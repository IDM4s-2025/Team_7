from experta import *

class SymptomsList(Fact):
    """A fact that contains a list of symptoms."""
    pass

class HematologyDiagnosis(KnowledgeEngine):
    """
    Rule engine for diagnosing hematological diseases.
    """

    # Anemia ferropénica (Iron Deficiency Anemia)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["fatigue", "paleness", "fragile nails"])))
    def iron_deficiency_anemia(self):
        self.declare(Fact(disease="Iron Deficiency Anemia",
                          explanation="Iron deficiency affecting the production of red blood cells",
                          recommendation="Consult a hematologist and increase iron intake"))

    # Anemia megaloblástica (Megaloblastic Anemia)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["fatigue", "yellow skin", "sore tongue"])))
    def megaloblastic_anemia(self):
        self.declare(Fact(disease="Megaloblastic Anemia",
                          explanation="Deficiency of vitamin B12 or folic acid",
                          recommendation="Requires blood tests and vitamin supplementation"))

    # Leucemia mieloide aguda (Acute Myeloid Leukemia, AML)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["fatigue", "fever", "bruises", "petechiae"])))
    def acute_myeloid_leukemia(self):
        self.declare(Fact(disease="Acute Myeloid Leukemia",
                          explanation="Cancer of the blood and bone marrow, resulting in an abnormal increase in white blood cells",
                          recommendation="Requires immediate medical attention, bone marrow biopsy"))

    # Leucemia linfoblástica aguda (Acute Lymphoblastic Leukemia, ALL)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["fatigue", "swollen lymph nodes", "night sweats"])))
    def acute_lymphoblastic_leukemia(self):
        self.declare(Fact(disease="Acute Lymphoblastic Leukemia",
                          explanation="Cancer of the lymphoid cells, causing symptoms like swollen lymph nodes and fever",
                          recommendation="Consult an oncologist for chemotherapy and other treatments"))

    # Linfoma no Hodgkin (Non-Hodgkin Lymphoma)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["swollen lymph nodes", "fever", "weight loss"])))
    def non_hodgkin_lymphoma(self):
        self.declare(Fact(disease="Non-Hodgkin Lymphoma",
                          explanation="Cancer of the lymphatic system that can cause swollen lymph nodes and night sweats",
                          recommendation="Consult an oncologist for diagnosis and treatment"))

    # Linfoma de Hodgkin (Hodgkin's Lymphoma)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["swollen lymph nodes", "night sweats", "weight loss"])))
    def hodgkins_lymphoma(self):
        self.declare(Fact(disease="Hodgkin's Lymphoma",
                          explanation="Cancer of the lymphatic system characterized by the presence of Reed-Sternberg cells",
                          recommendation="Consult an oncologist for chemotherapy and other treatments"))

    # Mieloma múltiple (Multiple Myeloma)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["bone pain", "fatigue", "weight loss"])))
    def multiple_myeloma(self):
        self.declare(Fact(disease="Multiple Myeloma",
                          explanation="Cancer of plasma cells in the bone marrow causing bone pain and fatigue",
                          recommendation="Requires medical evaluation and treatment with chemotherapy"))

    # Trombocitopatías (Platelet disorders)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["bleeding", "bruises", "nosebleed"])))
    def platelet_disorders(self):
        self.declare(Fact(disease="Platelet Disorders",
                          explanation="Conditions affecting platelet function or number, leading to bleeding and bruising",
                          recommendation="Consult a hematologist for platelet count and clotting tests"))

    # Hemofilia (Hemophilia)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["bruises", "bleeding", "nosebleed"])))
    def hemophilia(self):
        self.declare(Fact(disease="Hemophilia",
                          explanation="A genetic disorder that impairs blood clotting, leading to prolonged bleeding",
                          recommendation="Consult a hematologist for clotting factor replacement therapy"))

    # Púrpura trombocitopénica idiopática (Idiopathic Thrombocytopenic Purpura, ITP)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["bruises", "petechiae", "bleeding"])))
    def itp(self):
        self.declare(Fact(disease="Idiopathic Thrombocytopenic Purpura",
                          explanation="An autoimmune disorder causing low platelet count, leading to bruising and bleeding",
                          recommendation="Consult a hematologist for platelet count and possible treatments"))

    # Talassemia (Thalassemia)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["fatigue", "paleness", "weight loss"])))
    def thalassemia(self):
        self.declare(Fact(disease="Thalassemia",
                          explanation="A genetic blood disorder causing abnormal hemoglobin production",
                          recommendation="Requires genetic counseling and possible blood transfusions"))

    # Esferocitosis hereditaria (Hereditary Spherocytosis)
    @Rule(SymptomsList(symptoms=MATCH.symptoms),
          TEST(lambda symptoms: all(s in symptoms for s in ["fatigue", "paleness", "yellow skin"])))
    def hereditary_spherocytosis(self):
        self.declare(Fact(disease="Hereditary Spherocytosis",
                          explanation="A genetic condition causing abnormal red blood cells that break down easily, leading to anemia",
                          recommendation="Requires blood tests and possible splenectomy"))

def get_diagnosis(symptoms):
    engine = HematologyDiagnosis()
    engine.reset()
    print(f"Symptoms received: {symptoms}")
    engine.declare(SymptomsList(symptoms=symptoms))
    engine.run()
    return list(engine.facts.values())
