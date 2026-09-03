from find_paper import fetch_papers, print_papers


def main():
	"""程序主入口。"""
	keyword = input("请输入论文关键词（例如 machine learning）：").strip()
	if not keyword:
		print("关键词不能为空。")
		return

	try:
		papers = fetch_papers(keyword)
		print_papers(papers)
	except OSError as error:
		print(f"获取论文失败：{error}")


if __name__ == "__main__":
	main()
