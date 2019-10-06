#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <stack>
using namespace std;

const int MAX_NODE = 90000;

struct edgenode {
	int vertex_num;
	edgenode* next;
};

struct vertexnode {
	edgenode* first;
};

struct Graph {
	int n, e;
	vertexnode vnode[MAX_NODE];
};

Graph gra;
int time;
int dfn[MAX_NODE];
int low[MAX_NODE];
int vis[MAX_NODE];
int instack[MAX_NODE];
stack<int> set;

int sum = 0;
int max_cnt = -1;

void init(int n, int m) {
	for (int i = 1; i <= n; i++) {
		gra.vnode[i].first = NULL;
	}
	gra.n = n;
	gra.e = m;
}

void create_graph(int start, int end) {
	edgenode* p = new edgenode;
	p->vertex_num = end;
	p->next = gra.vnode[start].first;
	gra.vnode[start].first = p;
}

void tarjon(int x) {
	dfn[x] = low[x] = time++;
	set.push(x);
	vis[x] = 1;
	instack[x] = 1;
	edgenode* p = gra.vnode[x].first;
	while (p != NULL) {
		int cur = p->vertex_num;
		if (vis[cur] == 0) {
			tarjon(cur);
			low[x] = min(low[x], low[cur]);
		}
		else {
			low[x] = min(low[x], dfn[cur]);
		}
		p = p->next;
	}
	if (low[x] == dfn[x]) {
		sum++;
		int t;
		int cnt = 0;
		do {
			t = set.top();
			set.pop();
			cnt++;
			instack[t] = 0;
		} while (t != x);
		//cout << cnt << endl;
		max_cnt = max(max_cnt, cnt);
	}
}

int main() {

	ifstream input("clean.txt");
	ofstream output("res.txt");

	if (!input.is_open()) {
		cout << "not open" << endl;
	}

	int n, m;
	input >> n >> m;
	init(n, m);

	for (int i = 1; i <= n; i++) {
		dfn[i] = 0;
		low[i] = 0;
		vis[i] = 0;
		instack[i] = 0;
	}

	for (int i = 0; i < m; i++) {
		int start, end;
		input >> start >> end;
		create_graph(start, end);
	}

	cout << "cin done." << endl;

	for (int i = 1; i <= n; i++) {
		if (i % 10000 == 0) {
			//cout << i << "xixi" << i / 10000 << endl;
		}
		if (vis[i] == 0) {
			tarjon(i);
		}
	}


	output << "The total number of connected component is " << sum << endl;
	output << "The max amount of connected component is " << max_cnt << endl;

	return 0;
}