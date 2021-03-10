import aiohttp
from tqdm import tqdm


async def download_ipsw(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            name = url.split("/")[-1]
            with tqdm(
                total=int(resp.headers["content-length"], 0),
                unit="",
                desc=f"Downloading {name}: ",
                unit_divisor=1024,
                ascii=True,
                unit_scale=True,
            ) as bar:
                with open(f"results/{name}", "wb") as f:
                    async for chunk in resp.content.iter_chunked(1024):
                        f.write(chunk)
                        bar.update(len(chunk))
