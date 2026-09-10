🔹 Step 1: Install IntelliJ IDEA and Required Plugins

Download and install IntelliJ IDEA (Community or Ultimate) from JetBrains.
Install Scala Plugin:
Open IntelliJ IDEA → Go to File → Settings (Preferences on macOS).
Select Plugins → Search for "Scala" → Click Install.
Install Python Plugin:
Similarly, go to Plugins → Search for "Python" → Click Install.
🔹 Step 2: Create a New Project

Go to: File → New Project.
Choose Project Type:
Select Scala on the left panel if available.
Click Next and configure the Scala SDK (if not already installed, IntelliJ will prompt to download it).
Select Python as an additional framework if prompted (or we will add it later).
Click Finish to create the project.
🔹 Step 3: Configure Scala in the Project

Go to: File → Project Structure → Modules.
Select the project module → Click on the + button.
Select Scala → Choose Scala SDK.
Click Apply → OK.
🔹 Step 4: Configure Python in the Project

Go to: File → Settings → Project: YourProjectName → Python Interpreter.
Click Add Interpreter → Select Python version (install one if needed).
Set up the Python interpreter as:
System Interpreter (if Python is installed on your machine).
Virtual Environment (venv) for project isolation.
Click Apply → OK.
🔹 Step 5: Create Scala and Python Files

Now, you can have both Scala and Python files in the same project.

Right-click on the src folder → New → Scala Class.
Create a sample Scala file (Main.scala):
object Main {
def main(args: Array[String]): Unit = {
println("Hello from Scala!")
}
}
Similarly, create a Python file (script.py):
print("Hello from Python!")
🔹 Step 6: Run Scala and Python Files

Running Scala Code
Right-click on Main.scala → Click Run 'Main'.
Running Python Code
Right-click on script.py → Click Run 'script.py'.
🔹 Step 7: Enable Mixed Development (Optional)

If you want Scala and Python to interact:

Use Py4J to call Java/Scala code from Python.
Use Jep (Java Embedded Python) to call Python from Scala.
Example: Calling Python from Scala using Jep:

import jep._

object PythonIntegration {
def main(args: Array[String]): Unit = {
val jep = new Jep()
jep.eval("print('Hello from Python via Scala!')")
jep.close()
}
}
Ensure jep is installed using:

pip install jep
