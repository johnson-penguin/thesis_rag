import streamlit as st
import pyshark
import asyncio
import json

st.title("📡 5G Initial Access Progress Tracker (PCAP-Based)")

# Upload PCAP file
uploaded_file = st.file_uploader("Upload a PCAP file", type=["pcap", "pcapng"])

# Define signaling stage keywords to search in packets
stage_keywords = {
    "NG Setup": "ngsetup",
    "Initial UE Message": "initialuemessage",
    "NAS Authentication": "authentication",
    "NAS Security Mode": "security mode command",
    "UE Capability Transfer": "ueradiocapabilityinfoindication",
    "Initial Context Setup": "initialcontextsetup",
    "PDU Session Establishment": "pdusessionresourcesetup",
    "UE Context Release": "uecontextrelease"
}

config_fix_suggestions = {
    "NG Setup": "Check SCTP port and AMF IP in ngap.amf_ip",
    "NAS Authentication": "Check 5G auth parameters, SUCI/SUPI settings",
    "PDU Session Establishment": "Verify DNN and S-NSSAI match with SMF config",
    "UE Context Release": "UE may have lost connection, check RLC/MAC configs"
}

if uploaded_file:
    st.success(f"Uploaded file: {uploaded_file.name}")
    with open("temp.pcapng", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("Parsing PCAP file... this may take a few seconds")

    asyncio.set_event_loop(asyncio.new_event_loop())
    cap = pyshark.FileCapture("temp.pcapng", use_json=True, include_raw=False)

    progress_result = {stage: False for stage in stage_keywords}

    for pkt in cap:
        try:
            for stage, keyword in stage_keywords.items():
                if keyword in pkt._packet_string.lower():
                    progress_result[stage] = True
        except Exception:
            continue
    cap.close()

    st.markdown("### 📊 Access Progress")
    for stage, status in progress_result.items():
        if status:
            st.success(f"✅ {stage}")
        else:
            st.warning(f"⚠️ {stage} not completed")
            if stage in config_fix_suggestions:
                st.markdown(f"**Suggested Fix**: {config_fix_suggestions[stage]}")

    completed = sum(1 for s in progress_result.values() if s)
    total = len(progress_result)
    percent = (completed / total) * 100

    st.progress(percent / 100)
    st.metric(label="Access Progress", value=f"{percent:.0f}%", delta=f"{completed}/{total} steps completed")

    st.markdown("---")
    st.markdown("### 🔁 RAG Suggested Config Fix Snippet")
    st.code("""
gNodeBConfig.ngap.amf_ip = "192.168.70.141"
gNodeBConfig.slicing.s_nssai.sst = 1
gNodeBConfig.slicing.s_nssai.sd = "010203"
""", language="python")
else:
    st.info("Please upload a .pcap or .pcapng file to begin analysis.")
