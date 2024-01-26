from transformers import pipeline

# 仅指定任务时，使用默认模型（不推荐）
# pipe = pipeline(task="sentiment-analysis",model="/home/rr-ai/generic-sentiment_analysis-multilingual-v1")
pipe = pipeline(task="sentiment-analysis",model="/home/rr-ai/distilroberta-finetuned-financial-news-sentiment-analysis")
# pipe = pipeline(task="sentiment-analysis")

print(pipe("今儿上海可真冷啊"))

print(pipe("我觉得这家店蒜泥白肉的味道非常棒！"))