import sys, subprocess

class Compile:
    def __init__(self) -> None:
        self.softwareCode = sys.argv[1].replace(".kt", "") if sys.argv[1].endswith(".kt") == True else sys.argv[1]

        self.kotlinPath = "source\\kotlinc\\bin\\kotlinc.bat %s.kt -include-runtime -d source/compiled/%s.jar"%(self.softwareCode, self.softwareCode)
        self.javaCommand = f"java -jar source\\compiled\\{self.softwareCode}.jar {" ".join(sys.argv[2:])}"
        
    def Build(self):
        subprocess.call(self.kotlinPath)
        subprocess.call(self.javaCommand)


if __name__ == "__main__":
    Compile().Build()