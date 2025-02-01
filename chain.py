from Poem_RAG_generator.model import create_chat_groq
import Poem_RAG_generator.prompt as prompt
def generate_poem(topic):
    prompt_template = prompt.poem_generator_prompt_from_hub()
    llm = create_chat_groq()
    chain = prompt_template | llm
    response = chain.invoke({
        "topic" : topic
    })
    return response.content
