public class N_Queens{
    public static boolean isSafe(char[][] board,int x,int y,int n){
        //column check
        for(int row=0;row<x;row++){
            if(board[row][y]=='Q'){
                return false;
            }
        }
        //left diagonal
        int row=x;
        int col=y;
        while(row>=0&&col>=0){
            if(board[row][col]=='Q'){
                return false;
            }
            row--;
            col--;
        }
        //right diagonal
        row=x;
        col=y;
        while(row>=0&&col<n){
            if(board[row][col]=='Q'){
                return false;
            }
            row--;
            col++;
        }
        return true;

    }
    public static boolean place_queen(char[][] board,int x,int n){
        if(x>=n){
            return true;
        }
        for(int col=0;col<n;col++){
            if(isSafe(board,x,col,n)){
                board[x][col]='Q';
                if(place_queen(board, x+1, n)){
                    return true;
                }
                board[x][col]='.';
            }
        }
        return false;
    }
    public static void main(String[] args) {
        int n=4;
        char[][] board=new char[4][4];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                board[i][j]='.';
            }
        }
        if(place_queen(board, 0, n)){
            for(int i=0;i<n;i++){
                System.out.println();
                for(int j=0;j<n;j++){
                    System.out.print(board[i][j]+" ");
                }
            }
        }
    }
}