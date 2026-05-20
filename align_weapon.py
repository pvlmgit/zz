import os
import time
from playwright.sync_api import sync_playwright

def run_alignment_tests():
    print("Launching browser for micro-alignment tests...")
    # All tests use scale 0.8 and rot (0, 1.57, 0)
    alignments = [
        {"pos": (-0.22, 0.80, 0.10)},
        {"pos": (-0.22, 0.75, 0.10)},
        {"pos": (-0.22, 0.70, 0.10)},
        {"pos": (-0.22, 0.75, 0.05)},
        {"pos": (-0.22, 0.75, 0.15)},
        {"pos": (-0.20, 0.75, 0.10)},
    ]

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            page.on("console", lambda msg: print(f"[Browser Console] {msg.type}: {msg.text}"))
            
            page.goto("http://localhost:8000/tactical_ops_fixed.html")
            
            # Wait for loading screen to hide
            page.wait_for_selector("#loading-screen", state="hidden", timeout=20000)
            page.click("#btn-play")
            
            print("Waiting for playerWorldModel to load...")
            for _ in range(40):
                loaded = page.evaluate("window.playerWorldModel !== null && typeof window.playerWorldModel !== 'undefined' && window.playerWorldWeapon !== null && typeof window.playerWorldWeapon !== 'undefined'")
                if loaded:
                    print("playerWorldModel loaded successfully!")
                    break
                time.sleep(0.5)
            
            # Put in 3rd person camera mode
            page.evaluate("state.isFirstPerson = false;")
            
            for idx, align in enumerate(alignments, 1):
                pos = align['pos']
                print(f"Testing micro-align_{idx}: scale=0.8, pos={pos}, rot=(0, 1.57, 0)...")
                
                # Apply positioning
                page.evaluate(f"""
                    (() => {{
                        const weapon = window.playerWorldWeapon;
                        const model = window.playerWorldModel;
                        
                        state.isFirstPerson = false;
                        if (model) model.visible = true;
                        
                        // Set position/rotation
                        weapon.position.set({pos[0]}, {pos[1]}, {pos[2]});
                        weapon.rotation.set(0, 1.5708, 0);
                        
                        // Set scale to look normal size
                        weapon.scale.set(0.8, 0.8, 0.8);
                        
                        // Reset scale of external model to 1
                        weapon.traverse(n => {{
                            if (n.parent && n.parent.name === 'gunGroup' && n.name !== 'barrel' && n.name !== 'body' && n.name !== 'sight') {{
                                n.scale.set(1.0, 1.0, 1.0);
                            }}
                        }});
                    }})()
                """)
                
                # Wait for render
                page.wait_for_timeout(1000)
                
                # Take screenshot
                screenshot_path = f"C:\\Users\\Prince Vic Mayordo\\Downloads\\GAME\\align_{idx}.png"
                page.screenshot(path=screenshot_path)
                print(f"Saved screenshot to {screenshot_path}")
                
            browser.close()
            print("Micro-alignment tests completed.")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    run_alignment_tests()
