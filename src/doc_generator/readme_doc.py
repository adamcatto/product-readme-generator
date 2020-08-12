import typing
import re
from shutil import copyfile

README_STRUCTURE_PATH = '../includes/readme-template-structure.md'
README_OUTPUT_PATH = '../readme_output.md'

class Badge(object):
    def __init__(self, name=None, img_link=None, web_url=None):
        self.name = name
        self.img_link = img_link
        self.web_url = web_url

    def __repr__(self):
        if dict(filter(lambda value: value is not None, self.__dict__.items())) != {}:
            return '[![{0!s}][{1!s}]][{2!s}]'.format(self.name, self.img_link, self.web_url)
        else:
            return ''

# TODO: make this class a NamedTuple or enum? and then main class inherits from data class?
class ReadmeDocument(object):
    def __init__(self, 
                product_name: typing.AnyStr, 
                product_blurb: typing.AnyStr, 
                badge: typing.List[Badge],
                header_img_link: typing.AnyStr,
                installation_guide: typing.Dict[typing.AnyStr, typing.AnyStr],
                usage_example: typing.AnyStr,
                development_setup: typing.AnyStr,
                release_history: typing.Dict[typing.AnyStr, typing.List[typing.AnyStr]],
                **metadata) -> None: # metadata: typing.Dict[typing.Any, typing.Any]) -> None:

        self.product_name         = product_name
        self.product_blurb        = product_blurb
        self.badge                = badge
        self.header_img_link      = header_img_link
        self.installation_guide   = installation_guide
        self.usage_example        = usage_example
        self.development_setup    = development_setup
        self.release_history      = release_history
        self.metadata             = metadata

    # TODO: add setters that automatically `translate_to_markdown` on receiving new attribute values
    # TODO: (continued) use `sys.argv` for command-line updating; use Fire?
    # TODO: (continued) add functionality to create class by loading from json
    # TODO: (continued) add (classmethod) functionality to update markdown file upon witnessing changes to json file?

    _default_values = {
        'product_name': 'Product Name',
        'product_blurb': 'Product Blurb',
        'badge': None,
        'header_img_link': '../includes/example.png',
        'installation_guide': {
            'OS X & Linux': """```sh
                            npm install my-crazy-module --save```""",

            'Windows':"""
                    ```sh
                    edit autoexec.bat
                    ```"""
        },
        'usage_example': 'A few motivating and useful examples of how your product can be used.',
        'development_setup': '',
        'release_history': {
            '0.0.2': [
                'Change: fix typo',
                'Fix docstring'
            ],
            '0.0.1': [
                'initial commit'
            ]
        },
        'metadata': {
            'name': 'First M. Last',
            'github_account': 'foobar'
        }
    }

    def translate_to_markdown(self, input_file=README_STRUCTURE_PATH, output_file=README_OUTPUT_PATH):
        variables_to_include = list(dict(filter(lambda elem: elem is not None, self.__dict__.items())).keys())
        print(variables_to_include)
        with open(output_file, 'w') as output_file:
            with open(input_file, 'r') as input_file:
                for line in input_file:
                    result = re.search(r'\{\{\s*.*\s*\}\}', line)
                    if result:
                        bracketed_prop = result.group(0)
                        prop = bracketed_prop[3:-3] # remove double curly braces and spaces from each end
                        if prop in variables_to_include:
                            new_content = self.__dict__[prop]
                            output_file.write(line.replace(bracketed_prop, str(new_content)))
                        else:
                            output_file.write(line.replace(bracketed_prop, ''))
                    else:
                        output_file.write(line)



def reset_readme_doc():
    copyfile('../includes/readme-template-structure.md', '../readme_output.md')

#test
