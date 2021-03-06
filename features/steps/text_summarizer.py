@when(u'I go to the text summarizer')
def step_impl(context):
    context.browser.get('http://localhost:5000')

@then(u'I should see the text summarizer')
def step_impl(context):
    assert context.browser.title == "Text Analyzer"

@when(u'I submit the form with a valid string')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')
    text_to_parse = br.find_element_by_name("text_to_parse")
    text_to_parse.send_keys("valid string")
    br.find_element_by_id("submit").click()

@then(u'I should see the results page')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('results')
@when(u"I submit 'How much wood could a woodchuck chuck if a woodchuck could chuck wood' for text to analyze")
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')
    text_to_parse = br.find_element_by_name("text_to_parse")
    text_to_parse.send_keys("They refuse to permit us to obtain the refuse permit. How could they refuse us?")
    br.find_element_by_id("submit").click()

@then(u'I should see "Nouns: woodchuck:2, wood:2 and Verbs: chuck:2" displayed on the results page')
def step_impl(context):
    br = context.browser
    result = br.find_element_by_id('results').text
    assert result == "Nouns : [(u'How', 1), (u'refuse', 1), (u'permit.', 1)] | Verbs : [(u'refuse', 2), (u'obtain', 1), (u'permit', 1)]"
'''
'''