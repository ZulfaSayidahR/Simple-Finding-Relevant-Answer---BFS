from collections import deque

def find_relevant_answer(faq_graph, query):
    queue = deque([query])
    visited = set()

    while queue:
        current = queue.popleft()

        # Jika ditemukan dalam daftar jawaban, kembalikan jawaban tersebut
        if current in faq_graph["answers"]:
            return faq_graph["answers"][current]
        
        # Tandai sebagai telah dikunjungi
        visited.add(current)
        
        # Tambahkan pertanyaan terkait ke dalam antrian BFS jika belum dikunjungi
        if current in faq_graph:
            for neighbor in faq_graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return "No relevant answer found."

# Contoh FAQ Knowledge Graph
faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks are AI models inspired by the human brain.",
        "Supervised Learning": "Supervised Learning uses labeled data for training."
    }
}

# Contoh pencarian jawaban
query = "What is AI?"
answer = find_relevant_answer(faq_graph, query)
print(f"Relevant Answer: {answer}")
