#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

map<string, vector<string>> productions;
map<string, set<string>> first_sets;
map<string, set<string>> follow_sets;

set<string> visited;

void read_grammar(const string &file_name)
{
    ifstream file(file_name);
    string line;

    while (getline(file, line))
    {
        if (line.find("->") != string::npos)
        {
            string lhs = line.substr(0, line.find("->"));
            string rhs = line.substr(line.find("->") + 2);
            stringstream ss(rhs);
            string option;

            while (getline(ss, option, '|'))
            {
                productions[lhs].push_back(option);
            }
        }
    }
}

set<string> first(const string &symbol)
{
    if (visited.count(symbol))
    {
        return first_sets[symbol];
    }
    visited.insert(symbol);

    set<string> first_set;

    if (productions.find(symbol) == productions.end())
    { // Terminal symbol
        first_set.insert(symbol);
        return first_set;
    }

    for (const string &production : productions[symbol])
    {
        if (production == "ϵ")
        {
            first_set.insert("ϵ");
        }
        else
        {
            for (char c : production)
            {
                set<string> char_first = first(string(1, c));
                first_set.insert(char_first.begin(), char_first.end());
                if (char_first.find("ϵ") == char_first.end())
                {
                    break;
                }
            }
            if (production.find_first_not_of("ϵ") == string::npos)
            {
                first_set.insert("ϵ");
            }
        }
    }

    first_sets[symbol] = first_set;
    return first_set;
}

set<string> follow(const string &symbol)
{
    if (visited.count(symbol))
    {
        return follow_sets[symbol];
    }
    visited.insert(symbol);

    set<string> follow_set;

    if (symbol == productions.begin()->first)
    { // Start symbol
        follow_set.insert("$");
    }

    for (const auto &[lhs, rhs_list] : productions)
    {
        for (const string &rhs : rhs_list)
        {
            for (size_t i = 0; i < rhs.size(); ++i)
            {
                if (rhs[i] == symbol)
                {
                    if (i + 1 < rhs.size())
                    {
                        string next_symbol(1, rhs[i + 1]);
                        set<string> first_next = first(next_symbol);
                        follow_set.insert(first_next.begin(), first_next.end());
                        follow_set.erase("ϵ");
                        if (first_next.count("ϵ"))
                        {
                            follow_set.insert(follow(lhs));
                        }
                    }
                    else
                    {
                        if (lhs != symbol)
                        {
                            follow_set.insert(follow(lhs));
                        }
                    }
                }
            }
        }
    }

    follow_sets[symbol] = follow_set;
    return follow_set;
}

void compute_first_follow()
{
    for (const auto &[symbol, _] : productions)
    {
        first(symbol);
    }
    visited.clear();
    for (const auto &[symbol, _] : productions)
    {
        follow(symbol);
    }
}

int main()
{
    read_grammar("demo.txt");
    compute_first_follow();

    cout << "First:" << endl;
    for (const auto &[symbol, first_set] : first_sets)
    {
        cout << "Fr(" << symbol << ")={";
        for (const string &s : first_set)
        {
            cout << s << ", ";
        }
        cout << "\b\b}" << endl; // Remove last comma and space
    }

    cout << "Follow:" << endl;
    for (const auto &[symbol, follow_set] : follow_sets)
    {
        cout << "Fw(" << symbol << ")={";
        for (const string &s : follow_set)
        {
            cout << s << ", ";
        }
        cout << "\b\b}" << endl; // Remove last comma and space
    }

    return 0;
}