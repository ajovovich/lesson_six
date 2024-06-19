#Task 1: Product Review Analysis

python_reviews = [ 
    "This product is really good. I'm impressed with its quality.", 
    "The performance of this product is excellent. Highly recommended!", 
    "I had a bad experience with this product. It didn't meet my expectations.", 
    "Poor quality product. Wouldn't recommend it to anyone.", 
    "The product was average. Nothing extraordinary about it." ]

           
keywords = ["good", "bad", "Poor", "excellent", "average", ]

for review in python_reviews:
    for keyword in keywords:
        if keyword in review:
            modified_review = review.replace(keyword, keyword.upper())
            print(modified_review)

#Task 2: Sentiment Tally

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def review_tally():
    review_counts = {}  
    
    for review in python_reviews:
        positive_count = 0
        negative_count = 0

        for positive in positive_words:
            if positive.lower() in review.lower():
                positive_count += 1

        for negative in negative_words:
            if negative.lower() in review.lower():
                negative_count += 1

        review_counts[review] = (positive_count, negative_count)
        
    return review_counts

#Task 3: Review Summary

summary_reviews = []

for review in python_reviews:
    if len(review) <= 30:
        summary_reviews.append(review)
    else:
        space_index = review[:30].rfind(" ")
        if space_index != -1:
            summary_reviews.append(review[:space_index] + '...')
        else:
            summary_reviews.append(review[:30] + '...')
for summary in summary_reviews:
    print(summary)








    