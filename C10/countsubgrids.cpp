#include <bits/stdc++.h>
#define ll long long
#define endl "\n"
using namespace std;

ll n;
int main(){
    cin >> n;
    ll N=64;
    ll c=n/N+1;
    if(n%N==0){
        c--;
    }
    vector<vector<ll>> g(n);
    for(int i=0;i<n;i++){
        string s;
        cin >> s;
        for(int j=0;j<c;j++){
            ll k=0;
            int from=j*N;
            int to=min((j+1)*N,n);
            for(int z=from;z<to;z++){
                if(s[z]=='1'){
                    k+=1ll<<z%N;
                }
            }
            g[i].push_back(k);    

        }
    }
    ll ans=0;
    for(ll a=0;a<n-1;a++){
        for(ll b=a+1;b<n;b++){
            ll cnt=0;
            for(ll i=0;i<c;i++){
                cnt+=__builtin_popcountll(g[a][i]&g[b][i]);
            }
            ans+=cnt*(cnt-1)/2ll;

        }
    }

    cout << ans << endl;
    return 0;
}