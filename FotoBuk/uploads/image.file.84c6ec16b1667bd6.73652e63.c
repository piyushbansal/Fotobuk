#include <stdio.h>
#include <string.h>

int main()
{
	int i,j,k;
	int n,g=0,h=0;
	int temp;
		scanf("%d",&n);
		int m[n+1][n+1],w[n+1][n+1];
		for (j=1;j<=n;j++)
		{
			g++;
			for (k=0;k<=n;k++)
			{
				scanf("%d",&m[j][k]);
			}
		}
		for (j=1;j<=n;j++)
		{
			for (k=0;k<=n;k++)
			{
				scanf("%d",&w[j][k]);
			}
		}
		int unenm=n; //no. of unengaged men
		int un=1; //index of the unengaged man having the least index
		int men[n+1]; //-1 if unengaged, else index number of the woman engaged to
		int men2[n+1]; //stores the index number of his most preferred woman whom he hasn't asked yet
		//i.e. stores the number of proposals he has made+1
		int women[n+1];
		memset(men+1,-1,n*sizeof(int));
		memset(women+1,-1,n*sizeof(int));
		//memset(men2+1,1,n*sizeof(int)); //memset can't be used to set all the elements of an integer array as 1
		for (j=1;j<=n;j++) men2[j]=1;
		j=0;
		while (unenm!=0)
		{
			//j=0;
			while (men[j]!=-1) j++;
			//man no. j is unengaged. he proposes to men2[j].
			int wc=m[j][men2[j]];
			if (women[wc]==-1)
			{
				//wc and j get engaged
				women[wc]=j;men[j]=wc;unenm--;j=0;
			}
			else if (w[wc][women[wc]]>w[wc][j])
			{
				//wc and j get engaged, but total number of unemployed men remains same
				men[women[wc]]=-1;women[wc]=j;men[j]=wc;j=0;
			}
			//else keep j the same, so that this man can explore further options, until he gets engaged
			else
			{
				men2[j]++;
			}
		}
		for (j=1;j<=n;j++) printf("%d\n",men[j]);
	return 0;
} 
