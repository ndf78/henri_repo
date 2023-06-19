class Document_page:
    def __init__(self, url, consommation_co2, proprete_site):
        self.url = url
        self.consommation_co2 = consommation_co2
        self.proprete_site = proprete_site

    def get_url(self):
        return self.url

    def get_consommation_co2(self):
        return self.consommation_co2

    def get_proprete_site(self):
        return self.proprete_site


def renseigner_document(donnees_entre, class_document):
    HTML_File=open(f'{donnees_entre}','r')
    document = HTML_File.read().format(p=class_document)
    return document

def generer_rapport_html(donnees_entre, donnees_sortie, class_document):
    document = renseigner_document(donnees_entre, class_document)
    with open(f'{donnees_sortie}', 'w') as fichier:
        fichier.write(document)


generer_rapport_html('template/rapport_rse.html','rapport/exemple.html', Document_page("lapin1", "lapin2", "lapin3"))