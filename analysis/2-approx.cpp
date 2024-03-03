#include <bits/stdc++.h>
#include <chrono>
using namespace std;
#ifdef LOCAL
#include "/Users/ahshafi/Documents/cp/cp-template/Basic/debug.h"
#else
#define dbg1(args...)
#define dbg2(x)
#endif
const int N = 2e5 + 5;
vector<int> g[N];
int vis[N];
vector<int> w[4];
bool checkW3(int u)
{
    if(vis[u] == 1) return false; 
    vector<int> tmp;
    for(int i = (int)g[u].size() - 1; i >= 0 and tmp.size() < 2; i--)
    {
        int v = g[u][i];
        g[u].pop_back();
        if(!vis[v])
        {
            tmp.push_back(v);
        }
    }
    // dbg1(tmp.size());
    for(int v: tmp) 
        g[u].push_back(v);

    return tmp.size() >= 2;
}

bool checkW2(int v)
{
    if(vis[v] == 1) return false; 
    if(g[v].empty())
        return false;
    
    return checkW3(g[v].front());
        
}

bool checkW1(int v)
{
    if(vis[v] == 1) return false; 
    return !g[v].empty();
}


int findW(int idx, bool (*checker)(int))
{
    while(!w[idx].empty())
    {
        int v = w[idx].back();
        w[idx].pop_back();
        if(checker(v))
            return v;
        else
        {
            w[idx - 1].push_back(v);
        }

    }
    return -1;
}

vector<pair<int, int>> approximate()
{
    vector<pair<int, int>> maxlst;
    while(true)
    {
        // dbg1("hola");
        int v;
        v = findW(3, checkW3);
        // dbg1(v); 
        if(v != -1)
        {
            for(int u: g[v])
            {
                if(vis[u]) continue;
                w[3].push_back(u);
                maxlst.emplace_back(v, u);
                vis[u] = 2;
            }
            vis[v] = 1;
            continue;
        }

        v = findW(2, checkW2);
        // dbg1(v);
        if(v!= -1)
        {
            for(int u: g[v])
            {
                if(vis[u]) continue;
                w[3].push_back(u);
                maxlst.emplace_back(v, u);
                vis[u] = 2;
            }
            vis[v] = 1;
            continue;
        }

        v = findW(1, checkW1);
        // dbg1(v);
        if(v!= -1)
        {
            for(int u: g[v])
            {
                if(vis[u]) continue;
                w[3].push_back(u);
                maxlst.emplace_back(v, u);
                vis[u] = 2;
            }
            vis[v] = 1;
            continue;
        }
        else
            break;
    }

    return maxlst;
}
int deg[N];
int main()
{
    int n, m;
    cin >> n >> m;
    set<pair<int, int>> edges;
    for(int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        u++, v++;
        edges.emplace(u, v);
    }

    for(auto [u, v]: edges)
    {
        g[u].push_back(v);
        g[v].push_back(u);
    }
    vector<pair<int, int>> res;

    auto start = chrono::high_resolution_clock::now(); // Start time

    for(int i = 1; i <= n; i++)
    {
        if(vis[i]) continue;
        for(int j = 0; j < 4; j++)
            w[j].clear();

        w[3].push_back(i);
        vis[i] = 2;
        auto tres = approximate();
        for(auto e: tres)
            res.push_back(e);
    }

    auto end = chrono::high_resolution_clock::now(); // End time
    auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);
    cout << "Time taken: " << duration.count() << " milliseconds" << endl;


    int leafcnt = 0;

    for(auto [u, v]: res)
        deg[u]++, deg[v]++;
    

    for(int i = 1; i <= n; i++)
        leafcnt += deg[i] == 1;
    
    cout << "Leaf count: " << leafcnt << endl;
}
