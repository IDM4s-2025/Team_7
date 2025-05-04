from experta import Fact
from Expertaaa import get_diagnosis

def SioNo(answer):
    """
    Validates if the answer is affirmative (s) or negative (n)
    """
    while True:
        answer = answer.strip().lower()
        if answer == 's':
            return answer
        elif answer == 'n':
            return answer
        else:
            print("Please enter only 's' for Yes or 'n' for No")
            answer = input("Would you like to perform another diagnosis? (s/n): ")

def show_symptoms_menu():
    print("AVAILABLE SYMPTOMS:")
    print("0. I do not have any of these symptoms")
    symptoms = [
        "fatigue", "paleness", "fragile nails", "yellow skin", "sore tongue",
        "fever", "bleeding", "bruises", "swollen lymph nodes", "bone pain",
        "night sweats", "early satiety", "weight loss", "frequent fractures",
        "nosebleed", "petechiae", "joint pain", "slow growth",
        "dark urine", "itching after bathing", "dizziness", "headache"
    ]
    for i, symptom in enumerate(symptoms, 1):
        print(f"{i}. {symptom}")
    return symptoms

def get_user_symptoms():
    symptoms_list = show_symptoms_menu()
    while True:
        entry = input("\nEnter the numbers of your symptoms separated by commas (e.g., 1,3,5): ").strip()
        if entry == "0":
            return []
        try:
            numbers = [int(n.strip()) for n in entry.split(",")]
            selected = [symptoms_list[i-1] for i in numbers if 1 <= i <= len(symptoms_list)]
            if not selected:
                print("No valid symptoms were selected.")
            else:
                return selected
        except Exception:
            print("ERROR: Invalid input. Please enter numbers separated by commas (e.g., 1,3,5).")

def show_results(facts):
    diagnosis_found = False
    option_counter = 1  # Para numerar las opciones

    # Recorremos todos los hechos
    for fact in facts:
        if isinstance(fact, Fact) and hasattr(fact, 'get') and fact.get("disease"):
            # Si es el primer diagnóstico, no mostramos la opción, solo el diagnóstico.
            if option_counter > 1:
                print(f"\nOPCIÓN {option_counter}:")
            
            print(f"PRELIMINARY DIAGNOSIS: {fact['disease']}")
            print(f"EXPLANATION: {fact['explanation']}")
            print(f"RECOMMENDATION: {fact['recommendation']}")
            option_counter += 1  # Aumentamos el contador de opciones
            diagnosis_found = True

    if not diagnosis_found:
        print("\nNo specific diagnosis found for the symptoms entered.")
        print("General recommendation: Consult a hematologist for a more detailed evaluation.")

def main():
    print(""" 
WELCOME TO THE HEMATOLOGICAL DIAGNOSTIC EXPERT SYSTEM
This system helps to identify possible hematological diseases based on symptoms.
""")
    x = True
    while x:
        symptoms = get_user_symptoms()
        if not symptoms:
            print("No specific symptoms were entered.")
        else:
            print("Analyzing your symptoms...")
            facts = get_diagnosis(symptoms)
            show_results(facts)
        answer = input("Would you like to perform another diagnosis? (s/n): ")
        answer = SioNo(answer)
        if answer == "s":
            x = True
        else:
            print("Thank you.")
            x = False

main()

# EJEMPLOS DE COMBINACIONES VÁLIDAS DE SÍNTOMAS PARA EL DIAGNÓSTICO
# - [1, 2, 3] → Iron Deficiency Anemia (fatigue, paleness, fragile nails)
# - [1, 4, 5] → Megaloblastic Anemia (fatigue, yellow skin, sore tongue)
# - [1, 6, 7, 8] → Acute Myeloid Leukemia (fatigue, fever, bleeding, bruises)
# - [1, 9, 10] → Acute Lymphoblastic Leukemia (fatigue, swollen lymph nodes, night sweats)
# - [9, 6, 13] → Non-Hodgkin's Lymphoma (swollen lymph nodes, fever, weight loss)
# - [9, 10, 13] → Hodgkin's Lymphoma (swollen lymph nodes, night sweats, weight loss)
# - [14, 1, 13] → Multiple Myeloma (bone pain, fatigue, weight loss)
# - [7, 8, 15] → Platelet Disorders (bleeding, bruises, nosebleeds)
# - [7, 6, 8] → Hemophilia (bleeding, fever, bruises)
# - [7, 8, 16] → Idiopathic Thrombocytopenic Purpura (ITP) (bruises, petechiae, bleeding)
# - [1, 2, 13] → Thalassemia (fatigue, paleness, weight loss)
# - [1, 2, 4] → Hereditary Spherocytosis (fatigue, paleness, yellow skin)
# - [1, 2] → Iron Deficiency Anemia (fatigue, paleness)
# - [1, 3] → Megaloblastic Anemia (fatigue, fragile nails)
# - [1, 4] → Folic Acid Deficiency Anemia (fatigue, yellow skin)
# - [1, 5] → Vitamin B12 Deficiency Anemia (fatigue, sore tongue)
# - [1, 6] → Aplastic Anemia (fatigue, fever)
# - [1, 7] → Hemolytic Anemia (fatigue, bleeding)
# - [1, 8] → Anemia of Chronic Disease (fatigue, bruises)