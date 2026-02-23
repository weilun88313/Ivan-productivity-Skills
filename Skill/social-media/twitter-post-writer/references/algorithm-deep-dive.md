# X (Twitter) Algorithm Deep Dive

## System Architecture

### Home Mixer Pipeline

The recommendation system operates through three core stages:

#### 1. Candidate Sourcing

**In-Network Source (Thunder)**
- Fetches recent tweets from followed accounts
- Typically returns ~1,000 candidates
- Time-weighted: recent content prioritized
- Includes promoted content from followed accounts

**Out-of-Network Source (Phoenix Retrieval)**
- ML-powered discovery from global tweet corpus
- Uses embedding-based retrieval
- Analyzes user's historical engagement patterns
- Can surface viral content outside your network
- Returns ~1,000-5,000 candidates

#### 2. Ranking (Phoenix Scorer)

**Model Architecture**
- Transformer-based neural network (similar to GPT architecture)
- Trained on billions of user interactions
- Predicts multiple interaction probabilities simultaneously

**Predicted Probabilities**
The model outputs probability scores for:
- `P(favorite)` - User will like/favorite the tweet
- `P(repost)` - User will retweet/quote tweet
- `P(reply)` - User will write a reply
- `P(click)` - User will click to expand/view thread
- `P(profile_click)` - User will visit author's profile
- `P(dwell_time_long)` - User will spend >30s on tweet
- `P(video_view)` - User will watch attached video
- `P(photo_expand)` - User will expand attached photo
- `P(negative)` - User will block/mute/report

**Scoring Formula**
```
Final_Score = w1 × P(favorite)
            + w2 × P(repost)
            + w3 × P(reply)
            + w4 × P(click)
            + w5 × P(dwell_time_long)
            + w6 × P(video_view)
            + w7 × P(photo_expand)
            - w8 × P(negative)
```

Where `w1...w8` are learned weights that may vary by user segment.

**Important Notes**
- Weights are NOT public and may change
- Negative signals have strong negative weights
- Reply and retweet typically weighted higher than likes
- Long dwell time is a strong positive signal

#### 3. Filtering & Diversity

**Removal Filters**
- Already-seen tweets
- Blocked or muted authors
- Tweets with muted keywords
- Duplicate/near-duplicate content
- Quality filters (spam detection)

**Author Diversity Scorer**
- Reduces score for repeated appearances by same author
- Prevents timeline domination by single account
- Typical limit: 2-3 tweets per author per session

**Freshness Decay**
- Tweet score decreases with age
- Typical half-life: 6-24 hours depending on engagement velocity
- Viral tweets may remain visible longer

## Training Data & Feedback Loops

### Positive Training Signals
- Explicit: likes, retweets, replies, follows
- Implicit: click-throughs, dwell time, video completion rate
- Secondary: profile visits, saves (via link clicks), shares outside platform

### Negative Training Signals
- Explicit: blocks, mutes, reports, "not interested", unfollows
- Implicit: quick scroll-past (<1s dwell), back-button after click
- Secondary: app closes immediately after viewing tweet

### Feedback Loop Timing
- Real-time signals: clicks, dwell time, immediate engagement
- Delayed signals: likes/retweets within 24h still attributed
- Long-term signals: author reputation built over weeks/months

## Content Features Analyzed

### Text Features
- Sentiment (positive/negative/neutral)
- Topic classification
- Named entities (people, products, locations)
- Language complexity
- Presence of URLs
- Hashtag count and relevance
- Emoji usage patterns

### Author Features
- Historical engagement rates
- Follower count & growth rate
- Verification status
- Account age
- Previous content quality scores
- Violation history

### Engagement Context
- Time since user's last session
- User's recent interaction history
- Topic alignment with user interests
- Recency of user-author interactions

## Optimization Strategies

### For Maximum Reach (Impressions)

**Priority 1: Avoid Negative Signals**
- Single block/mute has outsized negative impact
- Report triggers immediate suppression
- "Not interested" teaches algorithm to avoid similar content

**Priority 2: Optimize for Retweets**
- Retweets amplify reach beyond your network
- Each retweet enters the scorer for new audiences
- Quote tweets count as enhanced retweets

**Priority 3: Drive Sustained Engagement**
- Threads that generate reply chains boost all tweets in thread
- Long dwell time signals quality content
- Saves (via bookmarks/links) indicate reference value

### For Maximum Engagement Rate

**Hook Optimization**
- First 50 characters determine click probability
- Question hooks increase reply probability
- Contrarian statements increase quote-tweet probability

**Reply Probability Boosters**
- Direct questions
- Opinion requests
- Incomplete information (curiosity gap)
- Personal anecdotes that invite sharing

**Retweet Probability Boosters**
- Quotable statements (standalone value)
- Useful resources/tools
- Novel insights or data
- Aligned with user's public identity

### For Author Growth

**Follow Probability**
- Consistent high-value content increases P(profile_click)
- Profile visits often lead to follows
- Multiple quality posts in user's feed increase familiarity

**Long-term Strategy**
- Regular posting builds engagement history
- Engagement on replies increases visibility
- Cross-engagement with related accounts expands network

## Algorithm Updates & Trends

### Known Changes (2024-2026)

**Increased Video Weight**
- Native video now has higher P(video_view) coefficient
- Short-form vertical video prioritized (TikTok-style)
- Video completion rate strongly impacts score

**De-emphasis on Bare Links**
- Tweets with only a URL see reduced reach
- Quote + insight format preferred
- Native content (text, images) prioritized

**Community Notes Impact**
- Tweets with Community Notes added see score reduction
- Multiple Community Notes can suppress account-wide
- Particularly affects misinformation

**Subscription (X Premium) Benefits**
- Verified accounts get mild score boost
- Longer tweet limit (4,000 chars) affects engagement patterns
- Edit feature reduces need for deletion/repost

### Predicted Future Directions

**Long-form Content**
- Platform push toward article-length posts
- May change optimal thread length
- Reading time could become explicit signal

**Creator-Subscriber Models**
- Paid subscribers may see algorithmic priority
- Subscription conversion could become a signal

## Common Myths Debunked

❌ **Myth**: "Posting at optimal times guarantees reach"
- **Reality**: Algorithm prioritizes engagement probability over timing. Good content surfaces regardless of post time.

❌ **Myth**: "More hashtags = more reach"
- **Reality**: Excessive hashtags (>3) correlate with spam and reduce engagement.

❌ **Myth**: "Follower count determines reach"
- **Reality**: Engagement rate matters more. High-follower accounts with low engagement see reduced reach.

❌ **Myth**: "Algorithm favors certain political views"
- **Reality**: Algorithm optimizes for engagement, which may favor controversial content regardless of direction.

❌ **Myth**: "External links are penalized"
- **Reality**: Context matters. Valuable resources with commentary perform well; bare link dumps don't.

## Technical Implementation Notes

### For Developers/Analysts

**API Considerations**
- Public API does not expose recommendation scores
- Impression data available via Twitter Analytics
- Engagement metrics accessible for owned content

**A/B Testing Approach**
- Test same content across different times/formats
- Minimum 100 impressions for statistical relevance
- Track engagement rate, not absolute numbers

**Measurement Framework**
```
Engagement Rate = (Likes + Retweets + Replies) / Impressions
Quality Score = (Retweets + Replies × 2) / Impressions
Virality Coefficient = Retweets / Impressions
```

## Ethical Considerations

### Responsible Optimization

**Do**:
- Create genuine value for audience
- Be transparent about intentions
- Build authentic engagement
- Respect platform norms

**Don't**:
- Manipulate through false information
- Use engagement bait tactically
- Artificially inflate metrics
- Exploit algorithm bugs

### Platform Health

The algorithm is designed to maximize user engagement, which doesn't always align with:
- Information accuracy
- Mental health
- Productive discourse
- Democratic values

Content creators should consider broader impact beyond algorithmic performance.

---

**Last Updated**: 2026-02-11
**Source**: X (xai-org) Algorithm Documentation on GitHub
