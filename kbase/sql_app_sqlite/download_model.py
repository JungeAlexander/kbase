from transformers import DistilBertModel, DistilBertTokenizer


model_class, tokenizer_class, pretrained_weights = (
    DistilBertModel,
    DistilBertTokenizer,
    "distilbert-base-cased",
)

# Load pretrained model/tokenizer
tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
model = model_class.from_pretrained(pretrained_weights)
