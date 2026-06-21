from fastapi import FastAPI

app = FastAPI(title="AUREXIA Backend")

creators = []
brands = []
campaigns = []
applications = []
escrows = []
dids=[]
zkp_proofs = []
ledger = []

@app.get("/")
def home():
    return {"message": "Welcome to AUREXIA Backend"}

@app.post("/creator")
def create_creator(
    name: str,
    niche: str,
    followers: int
):
    creator = {
        "name": name,
        "niche": niche,
        "followers": followers,
        "trust_score": 50
    }

    creators.append(creator)

    return creator

@app.post("/brand")
def create_brand(
    company: str,
    industry: str
):
    brand = {
        "company": company,
        "industry": industry
    }

    brands.append(brand)

    return brand

@app.post("/campaign")
def create_campaign(
    title: str,
    budget: int,
    niche: str
):
    campaign = {
        "title": title,
        "budget": budget,
        "niche": niche
    }

    campaigns.append(campaign)

    return campaign

@app.get("/creators")
def get_creators():
    return creators

@app.get("/campaigns")
def get_campaigns():
    return campaigns

@app.get("/trust-score/{followers}")
def trust_score(followers: int):

    if followers > 100000:
        score = 95
    elif followers > 10000:
        score = 80
    else:
        score = 60

    return {"trust_score": score}
@app.get("/match")
def match_creator(niche: str):

    matches = []

    for creator in creators:
        if niche.lower() in creator["niche"].lower():
            matches.append(creator)

    return matches
@app.post("/apply")
def apply_campaign(
    creator_name: str,
    campaign_title: str
):

    application = {
        "creator": creator_name,
        "campaign": campaign_title,
        "status": "Pending"
    }

    applications.append(application)

    return application
@app.get("/applications")
def get_applications():
    return applications
@app.get("/trust-agent")
def trust_agent(
    followers: int,
    verified: bool
):

    score = 50

    if followers > 10000:
        score += 20

    if followers > 100000:
        score += 15

    if verified:
        score += 15

    if score >= 85:
        status = "Highly Trusted"

    elif score >= 70:
        status = "Trusted"

    else:
        status = "Needs Verification"

    return {
        "trust_score": score,
        "trust_status": status
    }
@app.get("/ai-swarm")
def ai_swarm(
    niche: str,
    followers: int,
    verified: bool
):

    trust_score = 50

    if followers > 10000:
        trust_score += 20

    if followers > 100000:
        trust_score += 15

    if verified:
        trust_score += 15

    matched_creators = []

    for creator in creators:

        if niche.lower() in creator["niche"].lower():

            matched_creators.append(creator)

    return {
        "agent_1_matching": matched_creators,
        "agent_2_trust_score": trust_score,
        "agent_3_recommendation":
            "Recommended for campaign"
            if trust_score >= 70
            else "Needs verification"
    }
@app.post("/escrow")
def create_escrow(
    campaign_title: str,
    amount: int
):

    escrow = {
        "campaign": campaign_title,
        "amount": amount,
        "status": "Funds Locked"
    }

    escrows.append(escrow)

    return escrow
@app.get("/escrows")
def get_escrows():
    return escrows
@app.post("/did")
def create_did(
    user_name: str
):

    did = {
        "user": user_name,
        "did": f"did:aurexia:{user_name.lower()}",
        "verification_status": "Verified"
    }

    dids.append(did)

    return did
@app.get("/dids")
def get_dids():
    return dids
@app.post("/zkp")
def generate_zkp(
    user_name: str
):

    proof = {
        "user": user_name,
        "proof_id": f"zkp_{user_name.lower()}",
        "status": "Proof Generated"
    }

    zkp_proofs.append(proof)

    return proof
@app.post("/ledger")
def add_to_ledger(
    event_type: str,
    user_name: str
):

    transaction = {
        "transaction_id": len(ledger) + 1,
        "event": event_type,
        "user": user_name,
        "status": "Recorded On Chain"
    }

    ledger.append(transaction)

    return transaction
@app.get("/ledger")
def get_ledger():
    return ledger
@app.post("/verify-user")
def verify_user(
    user_name: str
):

    did = {
        "user": user_name,
        "did": f"did:aurexia:{user_name.lower()}",
        "status": "Created"
    }

    proof = {
        "user": user_name,
        "proof_id": f"zkp_{user_name.lower()}",
        "status": "Generated"
    }

    transaction = {
        "transaction_id": len(ledger) + 1,
        "event": "USER_VERIFIED",
        "user": user_name,
        "status": "Recorded On Chain"
    }

    ledger.append(transaction)

    return {
        "did": did,
        "zkp": proof,
        "ledger": transaction,
        "verification_status": "Verified"
    }
@app.post("/verify-user")
def verify_user(
    user_name: str
):

    did = {
        "user": user_name,
        "did": f"did:aurexia:{user_name.lower()}",
        "status": "Created"
    }

    proof = {
        "user": user_name,
        "proof_id": f"zkp_{user_name.lower()}",
        "status": "Generated"
    }

    transaction = {
        "transaction_id": len(ledger) + 1,
        "event": "USER_VERIFIED",
        "user": user_name,
        "status": "Recorded On Chain"
    }

    ledger.append(transaction)

    return {
        "did": did,
        "zkp": proof,
        "ledger": transaction,
        "verification_status": "Verified"
    }
# MULTIPLE AI AGENTS
# CREATOR DISCOVERY 
@app.get("/creator-discovery-agent")
def creator_discovery_agent(
    niche: str
):

    recommended_creators = []

    for creator in creators:

        if niche.lower() in creator["niche"].lower():

            recommended_creators.append({
                "creator_name": creator["name"],
                "niche": creator["niche"],
                "followers": creator["followers"],
                "match_score": 95
            })

    return {
        "agent": "Creator Discovery Agent",
        "recommendations": recommended_creators
    }

# AUDIENCE ANALYST 
@app.get("/audience-analyst-agent")
def audience_analyst_agent(
    creator_audience: str,
    target_audience: str
):

    if creator_audience.lower() == target_audience.lower():
        compatibility_score = 95
        recommendation = "Strong Audience Match"

    else:
        compatibility_score = 60
        recommendation = "Partial Audience Match"

    return {
        "agent": "Audience Analyst Agent",
        "creator_audience": creator_audience,
        "target_audience": target_audience,
        "compatibility_score": compatibility_score,
        "recommendation": recommendation
    }
# Campaign Strategist Agent
@app.get("/campaign-strategist-agent")
def campaign_strategist_agent(
    campaign_goal: str,
    budget: int
):

    if budget >= 50000:
        strategy = "Multi-platform Campaign"
        content_plan = "Reels, Stories, Posts"
        posting_frequency = "Daily"

    else:
        strategy = "Focused Campaign"
        content_plan = "Reels and Stories"
        posting_frequency = "3 times a week"

    return {
        "agent": "Campaign Strategist Agent",
        "campaign_goal": campaign_goal,
        "budget": budget,
        "strategy": strategy,
        "content_plan": content_plan,
        "posting_frequency": posting_frequency
    }
# TRUST MONITOR AGENT
@app.get("/trust-monitor-agent")
def trust_monitor_agent(
    trust_score: int,
    did_verified: bool,
    zkp_verified: bool
):

    if trust_score >= 85 and did_verified and zkp_verified:
        risk_level = "Low Risk"
        recommendation = "Trusted Creator"

    elif trust_score >= 70:
        risk_level = "Medium Risk"
        recommendation = "Additional Verification Recommended"

    else:
        risk_level = "High Risk"
        recommendation = "Not Recommended"

    return {
        "agent": "Trust Monitor Agent",
        "trust_score": trust_score,
        "did_verified": did_verified,
        "zkp_verified": zkp_verified,
        "risk_level": risk_level,
        "recommendation": recommendation
    }
# Performance Optimizer Agent
@app.get("/performance-optimizer-agent")
def performance_optimizer_agent(
    engagement_rate: float,
    reach: int
):

    if engagement_rate >= 5:
        performance = "High Performing"
        recommendation = "Scale Campaign Budget"

    elif engagement_rate >= 2:
        performance = "Average Performing"
        recommendation = "Optimize Content Strategy"

    else:
        performance = "Low Performing"
        recommendation = "Review Creator Selection"

    return {
        "agent": "Performance Optimizer Agent",
        "engagement_rate": engagement_rate,
        "reach": reach,
        "performance": performance,
        "recommendation": recommendation
    }
@app.post("/auth/creator/login")
def creator_login():
    return {
        "message": "Login route working"
    }