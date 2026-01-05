import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.title("🧗‍♂️ Case 3: The Dark Valley")

    # Checking for previous case completion
    if 'inventory_coordinates' not in st.session_state:
        st.error("⛔ Complete Case 2 first."); return

    if 'math_mode_3' not in st.session_state: st.session_state['math_mode_3'] = False
    
    # Text changes based on mode
    st.markdown("**Mission:** Guide the AI to the valley floor without errors." if not st.session_state['math_mode_3'] else "### 📐 Gradient Descent")

    lr = st.slider("Learning Rate (Alpha)", 0.01, 1.1, 0.1)
    
    x = np.linspace(-10, 10, 100); y = x**2
    pos = 8.0; path = [pos]
    
    for _ in range(10): 
        pos = pos - (lr * 2 * pos)
        path.append(pos)
        
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Error Function"); ax.plot(path, [p**2 for p in path], 'ro-', label="Path")
    ax.legend(); st.pyplot(fig)
    
    final_error = path[-1]**2
    
    st.subheader("📰 The Next Day's Headlines")
    if final_error < 0.1:
        st.success("HEADLINE: 'Watson AI Hits the Mark!'")
    elif final_error > 50:
        st.error("HEADLINE: 'SCANDAL! Hasty AI Labels Innocent Charity as Terrorists!'")
        # 'Mennan Usta' translated as 'Master Mennan' to keep the vibe
        st.write("**Master Mennan:** You trampled the garden trying to run too fast. **Accuracy** comes before speed.")
    else:
        st.warning("HEADLINE: 'Work in Progress...' (Insufficient Descent)")

    st.divider()
    if st.button("🔴 Red Pill"):
        st.session_state['math_mode_3'] = not st.session_state['math_mode_3']
        if hasattr(st, "rerun"): st.rerun() 
        else: st.experimental_rerun()

if __name__ == "__main__":
    run()