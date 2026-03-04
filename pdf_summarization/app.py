
    
    
import asyncio
from google.adk.runners import Runner
from agent import create_agent

async def main():

    agent = create_agent()
    runner = Runner(agent=agent)

    pdf_path = "C:\my_projects\ab9c40fa18286f5688a6acbd0ce08e38ef9fc3bf.pdf"
    user_message = f"Summarize the PDF located at: {pdf_path}"

    response = await runner.run(user_message)

    print("\n===== FINAL SUMMARY =====\n")
    print(response.output_text)

if __name__ == "__main__":
    asyncio.run(main())