# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:17:00 2026

@author: SREEKANTHVS
"""

import os
from agent import PDFSummarizationAgent

if __name__ == "__main__":

    api_key = os.getenv("OPENAI_API_KEY")

    agent = PDFSummarizationAgent(api_key=api_key)

    pdf_path = "C:\my_projects\melco_DATA\video_mix_aug_seminal_paper.pdf"

    summary = agent.summarize_pdf(pdf_path)

    print("\n\n===== FINAL SUMMARY =====\n")
    print(summary)