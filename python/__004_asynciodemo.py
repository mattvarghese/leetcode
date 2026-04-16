import asyncio
import httpx  # You may need to: pip install httpx

async def get_random_advice(request_id):
    url = "https://api.adviceslip.com/advice"
    
    # Use an async context manager for the client
    async with httpx.AsyncClient(timeout=60.0) as client:
        print(f"Request {request_id}: Fetching advice...")
        
        # 'await' here pauses this function until the API responds
        response = await client.get(url)
        
        data = response.json()
        advice = data['slip']['advice']
        
        print(f"Request {request_id} finished.")
        return advice

async def main():
    # 'asyncio.gather' fires all three requests at the SAME time
    # Instead of waiting 1s + 1s + 1s, it takes ~1s total.
    results = await asyncio.gather(
        get_random_advice(1),
        get_random_advice(2),
        get_random_advice(3)
    )

    print("\n--- Final Advice Received ---")
    for i, advice in enumerate(results, 1):
        print(f"{i}. {advice}")

if __name__ == "__main__":
    asyncio.run(main())