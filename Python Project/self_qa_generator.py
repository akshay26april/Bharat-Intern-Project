import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

def generate_qa_pairs(prompt_list, num_pairs=5):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    qa_pairs_list = []
    for prompt in prompt_list:
        # Encode the prompt
        input_ids = tokenizer.encode(prompt, return_tensors="pt")

        # Generate responses using the model
        outputs = model.generate(input_ids, max_length=50, num_return_sequences=num_pairs, num_beams=5, pad_token_id=tokenizer.eos_token_id)

        # Decode and format the responses as question and answer pairs
        qa_pairs = []
        for output in outputs:
            text = tokenizer.decode(output, skip_special_tokens=True)
            parts = text.split(prompt)
            if len(parts) > 1:
                question = prompt + parts[0]
                answer = parts[1].strip()
                qa_pairs.append({"question": question, "answer": answer})

        qa_pairs_list.extend(qa_pairs)

    return qa_pairs_list

if __name__ == "__main__":
    user_prompts = [
        "The capital of France is",
        "What is the meaning of life?",
        "Tell me a joke.",
        "How can I improve my productivity?",
        "Who is your favorite author?",
    ]

    generated_pairs = generate_qa_pairs(user_prompts, num_pairs=5)

    for i, pair in enumerate(generated_pairs, start=1):
        print(f"Question {i}: {pair['question']}")
        print(f"Answer {i}: {pair['answer']}")
        print()
