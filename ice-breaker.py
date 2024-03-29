from dotenv import load_dotenv
load_dotenv()
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAi

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello LangChain!")

linkedin_profile_url = linkedin_lookup_agent(name =" Quinton Mills")

summary_template = """"
    Given the LinkedIn information {information} about a person I want you to create:
    1. a short summary
    2. two interesting facts about them
"""

summary_prompt_template = PromptTemplate(
    input_variables = ["information"], template = summary_template
)

llm = ChatOpenAi(temperature = 0, model_name = "gpt-3.5-turbo")

chain = LLMChain(llm=llm, prompt = summary_prompt_template)
linkedin_data = scrape_linkedin_profile(linkedin_profile_url = linkedin_profile_url)

print(chain.invoke(input = {"information": linkedin_data}))

