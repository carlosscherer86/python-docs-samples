INPUT_DIV = '<div id="required" class="clearfix">'
HIDDEN_INPUT = '<input type="hidden" name="token" id="token" value="{0}">'

HOME_LINK = '<a href="/search">'
HOME_LINK_WITH_TOKEN = '<a href="/search?token={0}">'

SEARCH_LINK = '<a href="/search?'
SEARCH_LINK_WITH_TOKEN = '<a href="/search?token={0}&'

XML_SCRIPT = '%2Fxml%3F'
XML_SCRIPT_WITH_TOKEN = '%2Fxml%3Ftoken%3D{0}%26'
def add_token(response, token):
    print(response)
    reponseText = response.replace(INPUT_DIV, INPUT_DIV + HIDDEN_INPUT.format(token))
    reponseText = reponseText.replace(HOME_LINK, HOME_LINK_WITH_TOKEN.format(token))
    reponseText = reponseText.replace(SEARCH_LINK, SEARCH_LINK_WITH_TOKEN.format(token))
    reponseText = reponseText.replace(XML_SCRIPT, XML_SCRIPT_WITH_TOKEN.format(token))
    return reponseText