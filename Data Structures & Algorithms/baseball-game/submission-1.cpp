class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> result;

        for (int i = 0; i < operations.size(); i++)
        {
            if (operations[i] == "+")
            {
                result.push_back(result[result.size()-1] + result[result.size()-2]);
            }

            else if (operations[i] == "D")
            {
                result.push_back(result[result.size()-1] * 2);
            }

            else if (operations[i] == "C")
            {
                result.pop_back();
            }

            else
            {
                result.push_back(stoi(operations[i]));
            }


        }

        int sum = 0;

        for (int op : result)
        {
            sum += op;
        }

        return sum;
    }
};