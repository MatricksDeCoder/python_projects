import os
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
import wolframalpha
import wikipedia

path           = '~/Desktop/Completed_Projects/python_projects/Virtual_Assistant'
from dotenv import load_dotenv
project_folder = os.path.expanduser(path)
load_dotenv(os.path.join(project_folder, '.env'))
WOLFRAM_APP_ID = os.getenv("WOLFRAM_APP_ID")

client         = wolframalpha.Client(WOLFRAM_APP_ID)

while True:
    input          = raw_input("Ask your question:")
    try:
        res            = client.query(input)
        answer         = next(res.results).text
        print answer
    except:
        print wikipedia.summary(input, sentences=2)
