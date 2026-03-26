**Hello**🖐 **Automated Testing for Adactin Hotel App Website with Playwright, Pytest, POM, Allure Reports, and Jenkins Pipeline**

This project automates testing of the Adactin Hotel application, covering core features such as login, hotel search, and booking functionality. It is built to validate both standard workflows and edge-case scenarios.

Instead of only validating the happy path, tests cover multiple edge cases to ensure the system behaves correctly under various situations,
such as:
   - Logging in with invalid credentials 
   - Performing an invalid hotel search with missing or incorrect inputs 
   - Attempting to book a hotel with incomplete or invalid details 
   - Verifying system responses for unsuccessful booking attempts
___________________________________________

🎯 **Pre-requisites:**
- Python 3.11.9
- Any browsers(Chrome, Firefox, Edge)
- Browsers: Chrome, Firefox, Edge 
- Playwright installed (pip install playwright)
___________________________________________

▶ **Test Execution**

Run commands: 
1. Install Dependecies:

       pip install -r utilities/requirements.txt
2. Install Playwright browsers:

       playwright install
2. Run the test with Allure report:

       pytest -v --alluredir=reports/allure-result
   or specifying browser

       pytest -v --alluredir=reports/allure-result
    

**To run this on jenkins**
1. Add item name, click Pipeline and click OK
   <br>
   ![img.png](img.png) 
2. Scroll down and navigate to Pipeline then select "pipeline script from SCM" > Select Git > Paste the Repo URL and click Apply and Save
   <br>
   ![img_1.png](img_1.png)
3. Click build now
   <br>
   ![img_2.png](img_2.png)



    
   
   
    