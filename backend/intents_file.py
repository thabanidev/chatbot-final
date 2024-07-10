intents = [
    {
        "tag": "greeting",
        "patterns": ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "howdy", "hiya", "what's up", "greetings", "salutations", "how are you", "how's it going", "good day", "hi", "hello", "hey", "good morning", "good afternoon", "good evening", "howdy", "hiya", "what's up", "greetings", "salutations", "how are you", "how's it going", "good day"],
    },
    {
        "tag": "goodbye",
        "patterns": ["bye", "goodbye", "see you later", "thanks", "thank you", "see ya", "catch you later", "talk to you later", "farewell", "take care", "so long", "have a nice day", "thanks a lot", "bye", "goodbye", "see you later", "thanks", "thank you", "see ya", "catch you later", "talk to you later", "farewell", "take care", "so long", "have a nice day", "thanks a lot"],
    },
    {
        "tag": "order_status",
        "patterns": ["order status", "track order", "where is my order", "order information", "order details", "order tracking", "order update", "order progress", "order shipment", "order delivery", "order status update", "order details", "order information", "order", "tracking details", "tracking information", "tracking", "details details", "details information", "details", "information details", "information information", "information", "order tracking details", "order tracking information", "order tracking", "order update details", "order update information", "order update", "order progress details", "order progress information", "order progress", "order shipment details", "order shipment information", "order shipment", "order delivery details", "order delivery information", "order delivery", "order status update details", "order status update information", "order status update", "order details details", "order details information", "order details", "information details", "information information", "information", "order tracking details", "order tracking information", "order tracking", "order update details", "order update information", "order update", "order progress details", "order progress information", "order progress", "order shipment details", "order shipment information", "order shipment", "order delivery details", "order delivery information", "order delivery", "order status update details", "order status update information", "order status update"],
    },
    {
        "tag": "product_inquiry",
        "patterns": ["product information", "tell me about", "what is", "how does work", "product details", "specifications", "features", "product specs", "product features", "product overview", "product description", "product details", "product info", "product data", "product details", "product information", "product", "details details", "details information", "details", "information details", "information information", "information", "product details details", "product details information", "product details", "information details", "information information", "information", "product information details", "product information information", "product information", "product details details", "product details information", "product details", "information details", "information information", "information", "product information details", "product information information", "product information", "product details details", "product details information", "product details", "information details", "information information", "information"],
    },
    {
        "tag": "payment_issue",
        "patterns": ["payment failed", "payment problem", "refund", "chargeback", "payment error", "payment declined", "payment issue", "refund request", "refund status", "payment not working", "payment not processed", "refund process", "refund policy", "payment not received", "payment not received", "payment failed", "payment problem", "refund", "chargeback", "payment error", "payment declined", "payment issue", "refund request", "refund status", "payment not working", "payment not processed", "refund process", "refund policy", "payment not received", "payment not received"],
    },
    {
        "tag": "shipping_inquiry",
        "patterns": ["shipping", "delivery", "track package", "when will my order arrive", "shipping time", "delivery estimate", "shipping status", "shipping information", "delivery information", "delivery status", "shipping update", "package tracking", "package status", "when will my package arrive", "shipping tracking", "shipping details", "delivery details", "tracking details", "tracking information", "delivery tracking", "delivery details", "tracking details"],
    },
    {
        "tag": "return_policy",
        "patterns": ["return", "exchange", "refund policy", "return an item", "return process", "how to return", "return instructions", "how to exchange", "exchange process", "return item", "return policy details", "return policy information", "return policy", "return instructions", "how to return an item", "how to exchange an item", "exchange instructions", "refund policy", "refund instructions", "refund policy details", "refund policy information", "refund policy", "refund instructions", "refund policy details"],
    },
    {
        "tag": "complaint",
        "patterns": ["complaint", "issue", "problem", "not happy", "dissatisfied", "feedback", "concern", "complain", "report issue", "file complaint", "submit complaint", "complaint process", "customer service issue", "service complaint", "complaint details", "complaint information", "complaint", "issue details", "issue information", "issue", "problem details", "problem information", "problem", "not happy details", "not happy information", "not happy", "dissatisfied details", "dissatisfied information", "dissatisfied", "feedback details", "feedback information", "feedback", "concern details", "concern information", "concern", "complain details", "complain information", "complain", "report issue details", "report issue information", "report issue", "file complaint details", "file complaint information", "file complaint", "submit complaint details", "submit complaint information", "submit complaint"],
    },
    {
        "tag": "technical_support",
        "patterns": ["technical support", "troubleshooting", "help with", "doesn't work", "error message", "tech support", "support issue", "technical issue", "technical problem", "tech problem", "technical assistance", "help needed", "need help with", "technical details", "technical information", "technical", "issue details", "issue information", "issue", "problem details", "problem information", "problem", "not happy details", "not happy information", "not happy", "dissatisfied details", "dissatisfied information", "dissatisfied", "feedback details", "feedback information", "feedback", "concern details", "concern information", "concern", "complain details", "complain information", "complain", "report issue details", "report issue information", "report issue", "file complaint details", "file complaint information", "file complaint", "submit complaint details", "submit complaint information", "submit complaint"],
    },
    {
        "tag": "store_hours",
        "patterns": ["store hours", "opening hours", "closing time", "when are you open", "store timings", "store open time", "store close time", "business hours", "store operating hours", "what time do you open", "what time do you close", "store open hours", "store close hours", "store hours", "store operating hours", "store timings", "store hours details", "store hours information", "store hours", "opening hours details", "opening hours information", "opening hours", "closing time details", "closing time information", "closing time", "when are you open details", "when are you open information", "when are you open", "store open hours details", "store open hours information", "store open hours", "store close hours details", "store close hours information", "store close hours"],
    },
    {
        "tag": "account_help",
        "patterns": ["account", "profile", "login", "password reset", "update information", "account issue", "account problem", "profile update", "reset password", "forgot password", "change password", "account details", "update profile", "account support", "account assistance", "account details", "profile details", "login details", "password reset details", "reset password details", "change password details", "account issue details", "account problem details", "profile update details", "account support details", "account assistance details"],
    },
    {
        "tag": "fallback",
        "patterns": ["", "I don't understand", "Can you repeat?", "What did you say?", "Sorry, I didn't get that", "Could you say that again?", "I'm confused", "Can you clarify?", "Not sure what you mean", "Can you rephrase?", "I didn't catch that", "Say that again", "I don't understand", "Can you repeat?", "What did you say?", "Sorry, I didn't get that", "Could you say that again?", "I'm confused", "Can you clarify?", "Not sure what you mean", "Can you rephrase?", "I didn't catch that", "Say that again"],
    },
    {
        "tag": "positive_feedback",
        "patterns": ["yes", "that helped", "thank you", "great", "awesome", "perfect", "exactly", "problem solved", "that works", "all good", "thanks a lot", "you are great", "you are awesome", "appreciate it", "yes", "that helped", "thank you", "great", "awesome", "perfect", "exactly", "problem solved", "that works", "all good", "thanks a lot", "you are great", "you are awesome", "appreciate it"],
    },
    {
        "tag": "negative_feedback",
        "patterns": ["no", "not really", "not helpful", "still have a problem", "not solved", "didn't help", "didn't work", "still an issue", "still a problem", "unsatisfied", "unhappy", "not fixed", "didn't fix", "no", "not really", "not helpful", "still have a problem", "not solved", "didn't help", "didn't work", "still an issue", "still a problem", "unsatisfied", "unhappy", "not fixed", "didn't fix"],
    },
    {
        "tag": "end_conversation",
        "patterns": ["that's all", "I'm good", "no more questions", "done for now", "that's it", "all set", "nothing else", "no thanks", "all done", "finished", "all good", "I'm fine", "nothing more", "that's enough", "that's all", "I'm good", "no more questions", "done for now", "that's it", "all set", "nothing else", "no thanks", "all done", "finished", "all good", "I'm fine", "nothing more", "that's enough"],
    } 
]
