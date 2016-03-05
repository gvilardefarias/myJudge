#include <bits/stdc++.h>

using namespace std;

int n, dp[21][21][1001], mT=0, trufas[21][21][1001], x, y, t;

int pd(int posX, int posY, int temp, int cont){
	int a, b, c, d, e;

	if(posX<0 || posX>20)
		return 0;
	if(posY<0 || posY>20)
		return 0;
	if(temp>mT)
		return 0;	

	if(dp[posX][posY][temp] != -1)
		return dp[posX][posY][temp];	

	a = trufas[posX][posY][temp] + pd(posX+1, posY, temp+1, cont);
	b = trufas[posX][posY][temp] + pd(posX-1, posY, temp+1, cont);
	c = trufas[posX][posY][temp] + pd(posX, posY+1, temp+1, cont);
	d = trufas[posX][posY][temp] + pd(posX, posY-1, temp+1, cont);
	e = trufas[posX][posY][temp] + pd(posX, posY, temp+1, cont);

	dp[posX][posY][temp] = max(max(max(a,b),max(c,d)),e);

	return dp[posX][posY][temp];
}

int main(){
	scanf("%d",&n);

	for(int i=0;i<=20;i++)
		for(int j=0;j<=20;j++)
			for(int k=0;k<=1000;k++)
				trufas[i][j][k] = 0;

	for(int i=0;i<n;i++){
		scanf("%d %d %d",&x, &y, &t);

		trufas[x][y][t]++;

		if(t>mT)
			mT = t;
	}

	for(int i=0;i<=20;i++)
		for(int j=0;j<=20;j++)
			for(int k=0;k<=1000;k++)
				dp[i][j][k] = -1;
	
	printf("%d\n", pd(6,6,0,0));

	return 7;
}