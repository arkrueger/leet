/*
    approach:
        treat this like a depth first search
        check
*/

class Solution {
 public:
  // dfs approach
  vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor, int origColor = -1) {
    // if newColor = current color, don't do anything
    if (newColor == image[sr][sc]) {
      return image;
    }
    // if it's the first call, return the modified image after recursing
    if (origColor == -1) {
      // recurse with the correct origColor
      floodFill(image, sr, sc, newColor, image[sr][sc]);
      // return the modified image
      return image;
    }

    // if it's not the first function call, recurse (or not) accordingly

    // if the current cell is not the original color, return early
    // (we reached the border and do not want to change this cell's color, nor check adjacents)
    if (image[sr][sc] != origColor) {
      return image;
    }

    // modify the current cell's color
    image[sr][sc] = newColor;
    // recurse on the 4 adjacent cells as long as they're in bounds
    if (sr < image.size() - 1) {
      floodFill(image, sr + 1, sc, newColor, origColor);
    }
    if (sc < image[0].size() - 1) {
      floodFill(image, sr, sc + 1, newColor, origColor);
    }
    if (sr > 0) {
      floodFill(image, sr - 1, sc, newColor, origColor);
    }
    if (sc > 0) {
      floodFill(image, sr, sc - 1, newColor, origColor);
    }

    // return
    return image;
  }
};