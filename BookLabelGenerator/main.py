from tqdm import tqdm
import json
import openai

openai.organization = "org-dpKom7PIpwoIeV44FCpAxa36"
openai.api_key = "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"

book_list_file = open('list.txt', 'r')
book_list = book_list_file.readlines()
label_dict = {}

for i, book in enumerate(tqdm(book_list)):
    title_author = book.split(' by ')
    title, author = title_author[0], title_author[1]

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Introduce me the book \"{title}\" by {author}, in detail, within 4 sentences. Tell briefly about the book, its genre and the plot.\n",
        temperature=0.8,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_text = response["choices"][0]["text"].split("\n\n")[0]
    label_dict[i] = f'{title}\nby {author}\n\n{response_text}'

with open('labels.json', 'w') as file:
    json.dump(label_dict, file, indent=4)