"""

    Title: test_survey.py
    Author: Eric Matthes
    Date: 04/28/2023
    Description: "Let's write a test that verifies one aspect of the way 
    AnonymousSurvey behaves. We'll write a test to verify that a single 
    response to the survey question is stored properly:"

"""

from survey import AnonymousSurvey

def test_store_single_response():

    # Test that a single response is stored properly:
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


"""

    "This is a good start, but a survey is useful only if it generates more 
    than one response. Let's verify that three responses can be stored 
    correctly. To do this, we add another method to **TestAnonymousSurvey**:"

"""

def test_store_tree_responses():

    # Test that three individual responses are stored properly. 
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses


"""

    "This works perfectly. However, these tests are a bit repetitive, so we'll 
    use another feature of pytest to make them more efficient."

"""

