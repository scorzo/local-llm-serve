from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
app = Flask(__name__)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    inputs = tokenizer(data['prompt'], return_tensors="pt")
    max_new_tokens = data.get('max_new_tokens', 100)  # Default to 50 if not provided
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'response': response})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
