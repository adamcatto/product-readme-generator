from readme_doc import *

# Test

if __name__ == "__main__":

    b = Badge('a','b','c')
    bc = Badge()
    print(b)
    print(bc)

    reset_readme_doc()

    doc = ReadmeDocument(
        'my product',
        'blurb',
        [Badge()],
        '',
        {'MacOS': 'uh, not sure'},
        'go like this',
        'dev-setup',
        {'0.0.1': ['did something', 'did something else']},
        #{'name': 'adam', 'github-username': 'adamcatto'}
        name='adam',
        github='adamcatto'
    )
    print(doc.badge[0])
    doc.translate_to_markdown()

