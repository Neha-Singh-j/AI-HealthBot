import streamlit as st
from chatbot.chatbot_logic import predict_disease, top_symptoms

# Configure page
st.set_page_config(page_title="AI Doctor", layout="centered")
st.title("🤖 Medical Diagnosis Assistant")

# Input section
symptoms_input = st.text_input(
    "Enter your symptoms (comma separated)",
    "",
    placeholder="e.g., fever, headache, cough",
    help="Separate multiple symptoms with commas"
)

if st.button("Diagnose"):
    if not symptoms_input.strip():
        st.error("⚠️ Please enter at least one symptom")
        st.stop()
    
    # Process symptoms
    symptoms = [
        s.strip().lower().replace(" ", "_") 
        for s in symptoms_input.split(",") 
        if s.strip()
    ]
    
    if not symptoms:
        st.error("⚠️ No valid symptoms detected")
        st.stop()
    
    with st.spinner("🔍 Analyzing symptoms..."):
        try:
            result = predict_disease(symptoms)
            
            # Ensure all required fields exist
            result.setdefault('disease', 'Unknown')
            result.setdefault('description', 'No description available')
            result.setdefault('precautions', ['Consult a doctor'])
            result.setdefault('severity', 'Unknown')
            
            # Display results
            st.subheader("Diagnosis Results")
            
            cols = st.columns([1,1,2])
            with cols[0]:
                st.markdown("**Condition**")
                st.info(result['disease'])
            
            with cols[1]:
                st.markdown("**Severity**")
                if result['severity'] == "Serious":
                    st.error("🆘 Serious")
                else:
                    st.warning(f"⚠️ {result['severity']}")
            
            with cols[2]:
                st.markdown("**Description**")
                st.write(result['description'])
            
            st.markdown("**Recommended Actions**")
            if result['precautions']:
                for i, action in enumerate(result['precautions'], 1):
                    st.write(f"{i}. {action}")
            else:
                st.info("No specific precautions - please consult a doctor")
                
        except Exception as e:
            st.error(f"❌ Diagnosis failed: {str(e)}")
            if st.checkbox("Show technical details"):
                st.exception(e)

# Show severe symptoms
with st.expander("⚠️ Top Severe Symptoms"):
    try:
        severe_symptoms = top_symptoms()
        if severe_symptoms:
            st.write(", ".join(severe_symptoms))
        else:
            st.warning("Could not load severe symptoms list")
    except:
        st.warning("Error loading severe symptoms")