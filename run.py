import asyncio
import json
from pathlib import Path
import indeed

output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)


async def run():
    indeed.BASE_CONFIG["cache"] = True

    print("running Indeed scrape and saving results to ./results directory")
# change what you want to scrape here, python is what field i want to scrape and Spokane is where i want to scrape
    url = "https://www.indeed.com/jobs?q=python&l=Spokane"
    result_search = await indeed.scrape_search(url, max_results=100)
    output.joinpath("search.json").write_text(json.dumps(result_search, indent=2, ensure_ascii=False))

    jobs = ["4c1e2988b22fa223", "483d39cbe1b6c1fe"]
    result_jobs = await indeed.scrape_jobs(jobs)
    output.joinpath("jobs.json").write_text(json.dumps(result_jobs, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(run())
