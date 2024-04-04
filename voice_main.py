from voice_settings import requirements
from voice_function import voice_speak, voice_list

if __name__ == "__main__":
    requirements(False)    
    #Type 1
    voice_speak(["I want speak"])
    #Type 2    
    voice_speak(["I", "want", "speak"])
    #Type 3 - Default    
    voice_speak()
