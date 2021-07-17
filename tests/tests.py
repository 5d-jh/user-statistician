# user-statistician: Github action for generating a user stats card
# 
# Copyright (c) 2021 Vincent A Cicirello
# https://www.cicirello.org/
#
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import unittest

import sys
sys.path.insert(0,'src')
from Statistician import *
from StatsImageGenerator import StatsImageGenerator
from Colors import *
from StatConfig import *
import copy

executedQueryResults = [
    {'data': {'user': {'contributionsCollection': {'totalCommitContributions': 3602, 'totalIssueContributions': 79, 'totalPullRequestContributions': 289, 'totalPullRequestReviewContributions': 315, 'totalRepositoryContributions': 18, 'restrictedContributionsCount': 105, 'contributionYears': [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011]}, 'followers': {'totalCount': 9}, 'following': {'totalCount': 7}, 'issues': {'totalCount': 81}, 'login': 'cicirello', 'name': 'Vincent A. Cicirello', 'pullRequests': {'totalCount': 289}, 'repositoriesContributedTo': {'totalCount': 3}, 'sponsorshipsAsMaintainer': {'totalCount': 7}, 'sponsorshipsAsSponsor': {'totalCount': 5}}}},

    [{'data': {'user': {'repositories': {'totalCount': 31, 'nodes': [{'stargazerCount': 0, 'forkCount': 0, 'isArchived': True, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 7139, 'edges': [{'size': 7139, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 4, 'totalSize': 1479512, 'edges': [{'size': 1309108, 'node': {'color': '#e34c26', 'name': 'HTML'}}, {'size': 168479, 'node': {'color': '#3D6117', 'name': 'TeX'}}, {'size': 1721, 'node': {'color': '#563d7c', 'name': 'CSS'}}, {'size': 204, 'node': {'color': '#f1e05a', 'name': 'JavaScript'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 5842, 'edges': [{'size': 5842, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 3, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 45961, 'edges': [{'size': 44035, 'node': {'color': '#b07219', 'name': 'Java'}}, {'size': 1926, 'node': {'color': '#89e051', 'name': 'Shell'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': True, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 7717, 'edges': [{'size': 7717, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 8491, 'edges': [{'size': 8491, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 0, 'forkCount': 3, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 2}, 'languages': {'totalCount': 1, 'totalSize': 74003, 'edges': [{'size': 74003, 'node': {'color': '#3572A5', 'name': 'Python'}}]}}, {'stargazerCount': 3, 'forkCount': 2, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 739339, 'edges': [{'size': 739339, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 2, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 52285, 'edges': [{'size': 52285, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 7, 'forkCount': 4, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 2100055, 'edges': [{'size': 2100055, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 3, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 3, 'totalSize': 266774, 'edges': [{'size': 198236, 'node': {'color': '#b07219', 'name': 'Java'}}, {'size': 34345, 'node': {'color': '#3D6117', 'name': 'TeX'}}, {'size': 34193, 'node': {'color': '#e34c26', 'name': 'HTML'}}]}}, {'stargazerCount': 3, 'forkCount': 2, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 39091, 'edges': [{'size': 38882, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 209, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}, {'stargazerCount': 0, 'forkCount': 1, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 852, 'edges': [{'size': 852, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 787, 'edges': [{'size': 787, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 1, 'forkCount': 2, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 1412, 'edges': [{'size': 1412, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}, {'stargazerCount': 2, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 31866, 'edges': [{'size': 31656, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 210, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 692, 'edges': [{'size': 692, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 2, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 4, 'totalSize': 36101, 'edges': [{'size': 26436, 'node': {'color': '#b07219', 'name': 'Java'}}, {'size': 7807, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 1758, 'node': {'color': '#427819', 'name': 'Makefile'}}, {'size': 100, 'node': {'color': '#C1F12E', 'name': 'Batchfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 107241, 'edges': [{'size': 106048, 'node': {'color': '#b07219', 'name': 'Java'}}, {'size': 1193, 'node': {'color': '#427819', 'name': 'Makefile'}}]}}, {'stargazerCount': 1, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': True, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 1943, 'edges': [{'size': 1469, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 474, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 9, 'forkCount': 14, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 2}, 'languages': {'totalCount': 2, 'totalSize': 46228, 'edges': [{'size': 45994, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 234, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 91844, 'edges': [{'size': 90353, 'node': {'color': '#b07219', 'name': 'Java'}}, {'size': 1491, 'node': {'color': '#427819', 'name': 'Makefile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 1984, 'edges': [{'size': 1763, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 221, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 3, 'totalSize': 75220, 'edges': [{'size': 72961, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 1902, 'node': {'color': '#e10098', 'name': 'GraphQL'}}, {'size': 357, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': True, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 0}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': True, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 0}, 'languages': {'totalCount': 7, 'totalSize': 1415534, 'edges': [{'size': 998990, 'node': {'color': '#f1e05a', 'name': 'JavaScript'}}, {'size': 247728, 'node': {'color': '#2b7489', 'name': 'TypeScript'}}, {'size': 127643, 'node': {'color': '#e34c26', 'name': 'HTML'}}, {'size': 26509, 'node': {'color': '#c6538c', 'name': 'SCSS'}}, {'size': 5854, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 5303, 'node': {'color': '#89e051', 'name': 'Shell'}}, {'size': 3507, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}], 'pageInfo': {'hasNextPage': False, 'endCursor': 'Y3Vyc29yOnYyOpHOFwfoDg=='}}}}}],

    [{'data': {'user': {'watching': {'totalCount': 28, 'nodes': [{'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}], 'pageInfo': {'hasNextPage': False, 'endCursor': 'Mjg'}}}}}],

    {'data': {'user': {'year2021': {'totalCommitContributions': 1850, 'totalPullRequestReviewContributions': 223, 'restrictedContributionsCount': 105}, 'year2020': {'totalCommitContributions': 1845, 'totalPullRequestReviewContributions': 92, 'restrictedContributionsCount': 0}, 'year2019': {'totalCommitContributions': 194, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2018': {'totalCommitContributions': 198, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2017': {'totalCommitContributions': 177, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2016': {'totalCommitContributions': 138, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2015': {'totalCommitContributions': 0, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2014': {'totalCommitContributions': 0, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2013': {'totalCommitContributions': 0, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2012': {'totalCommitContributions': 0, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2011': {'totalCommitContributions': 0, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}}}},

    [{'data': {'user': {'topRepositories': {'totalCount': 34, 'nodes': [{'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'someUserA'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'someUserA'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'someUserB'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'someUserC'}}, {'owner': {'login': 'someUserD'}}, {'owner': {'login': 'someUserE'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'someUserA'}}, {'owner': {'login': 'someUserF'}}], 'pageInfo': {'hasNextPage': False, 'endCursor': 'MzQ'}}}}}]
    ]

executedQueryResultsTest2 = copy.deepcopy(executedQueryResults)

executedQueryResultsMultiPage = [
    {'data': {'user': {'contributionsCollection': {'totalCommitContributions': 3602, 'totalIssueContributions': 79, 'totalPullRequestContributions': 289, 'totalPullRequestReviewContributions': 315, 'totalRepositoryContributions': 18, 'restrictedContributionsCount': 105, 'contributionYears': [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011]}, 'followers': {'totalCount': 9}, 'following': {'totalCount': 7}, 'issues': {'totalCount': 81}, 'login': 'cicirello', 'name': 'Vincent A. Cicirello', 'pullRequests': {'totalCount': 289}, 'repositoriesContributedTo': {'totalCount': 3}, 'sponsorshipsAsMaintainer': {'totalCount': 7}, 'sponsorshipsAsSponsor': {'totalCount': 5}}}},

    [{'data': {'user': {'repositories': {'totalCount': 31, 'nodes': [{'stargazerCount': 0, 'forkCount': 0, 'isArchived': True, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 7139, 'edges': [{'size': 7139, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 4, 'totalSize': 1479512, 'edges': [{'size': 1309108, 'node': {'color': '#e34c26', 'name': 'HTML'}}, {'size': 168479, 'node': {'color': '#3D6117', 'name': 'TeX'}}, {'size': 1721, 'node': {'color': '#563d7c', 'name': 'CSS'}}, {'size': 204, 'node': {'color': '#f1e05a', 'name': 'JavaScript'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 5842, 'edges': [{'size': 5842, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 3, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 45961, 'edges': [{'size': 44035, 'node': {'color': '#b07219', 'name': 'Java'}}, {'size': 1926, 'node': {'color': '#89e051', 'name': 'Shell'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': True, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 7717, 'edges': [{'size': 7717, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 8491, 'edges': [{'size': 8491, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 0, 'forkCount': 3, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 2}, 'languages': {'totalCount': 1, 'totalSize': 74003, 'edges': [{'size': 74003, 'node': {'color': '#3572A5', 'name': 'Python'}}]}}, {'stargazerCount': 3, 'forkCount': 2, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 739339, 'edges': [{'size': 739339, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 2, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 52285, 'edges': [{'size': 52285, 'node': {'color': '#b07219', 'name': 'Java'}}]}}, {'stargazerCount': 7, 'forkCount': 4, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 2100055, 'edges': [{'size': 2100055, 'node': {'color': '#b07219', 'name': 'Java'}}]}}], 'pageInfo': {'hasNextPage': True, 'endCursor': 'Y3Vyc29yOnYyOpHOEEbJCQ=='}}}}}, {'data': {'user': {'repositories': {'totalCount': 31, 'nodes': [{'stargazerCount': 3, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 3, 'totalSize': 266774, 'edges': [{'size': 198236, 'node': {'color': '#b07219', 'name': 'Java'}}, {'size': 34345, 'node': {'color': '#3D6117', 'name': 'TeX'}}, {'size': 34193, 'node': {'color': '#e34c26', 'name': 'HTML'}}]}}, {'stargazerCount': 3, 'forkCount': 2, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 39091, 'edges': [{'size': 38882, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 209, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}, {'stargazerCount': 0, 'forkCount': 1, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 852, 'edges': [{'size': 852, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 787, 'edges': [{'size': 787, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 1, 'forkCount': 2, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 1412, 'edges': [{'size': 1412, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}, {'stargazerCount': 2, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 31866, 'edges': [{'size': 31656, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 210, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 1, 'totalSize': 692, 'edges': [{'size': 692, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 2, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 4, 'totalSize': 36101, 'edges': [{'size': 26436, 'node': {'color': '#b07219', 'name': 'Java'}}, {'size': 7807, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 1758, 'node': {'color': '#427819', 'name': 'Makefile'}}, {'size': 100, 'node': {'color': '#C1F12E', 'name': 'Batchfile'}}]}}], 'pageInfo': {'hasNextPage': True, 'endCursor': 'Y3Vyc29yOnYyOpHOEcjkCw=='}}}}}, {'data': {'user': {'repositories': {'totalCount': 31, 'nodes': [{'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 107241, 'edges': [{'size': 106048, 'node': {'color': '#b07219', 'name': 'Java'}}, {'size': 1193, 'node': {'color': '#427819', 'name': 'Makefile'}}]}}, {'stargazerCount': 1, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': True, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 1943, 'edges': [{'size': 1469, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 474, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 9, 'forkCount': 14, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 2}, 'languages': {'totalCount': 2, 'totalSize': 46228, 'edges': [{'size': 45994, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 234, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 91844, 'edges': [{'size': 90353, 'node': {'color': '#b07219', 'name': 'Java'}}, {'size': 1491, 'node': {'color': '#427819', 'name': 'Makefile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 2, 'totalSize': 1984, 'edges': [{'size': 1763, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 221, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': False, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 1}, 'languages': {'totalCount': 3, 'totalSize': 75220, 'edges': [{'size': 72961, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 1902, 'node': {'color': '#e10098', 'name': 'GraphQL'}}, {'size': 357, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}, {'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': True, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 0}, 'languages': {'totalCount': 0, 'totalSize': 0, 'edges': []}}], 'pageInfo': {'hasNextPage': True, 'endCursor': 'Y3Vyc29yOnYyOpHOFvwXeA=='}}}}}, {'data': {'user': {'repositories': {'totalCount': 31, 'nodes': [{'stargazerCount': 0, 'forkCount': 0, 'isArchived': False, 'isFork': True, 'isPrivate': False, 'isTemplate': False, 'watchers': {'totalCount': 0}, 'languages': {'totalCount': 7, 'totalSize': 1415534, 'edges': [{'size': 998990, 'node': {'color': '#f1e05a', 'name': 'JavaScript'}}, {'size': 247728, 'node': {'color': '#2b7489', 'name': 'TypeScript'}}, {'size': 127643, 'node': {'color': '#e34c26', 'name': 'HTML'}}, {'size': 26509, 'node': {'color': '#c6538c', 'name': 'SCSS'}}, {'size': 5854, 'node': {'color': '#3572A5', 'name': 'Python'}}, {'size': 5303, 'node': {'color': '#89e051', 'name': 'Shell'}}, {'size': 3507, 'node': {'color': '#384d54', 'name': 'Dockerfile'}}]}}], 'pageInfo': {'hasNextPage': False, 'endCursor': 'Y3Vyc29yOnYyOpHOFwfoDg=='}}}}}],

    [{'data': {'user': {'watching': {'totalCount': 28, 'nodes': [{'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}], 'pageInfo': {'hasNextPage': True, 'endCursor': 'MTA'}}}}}, {'data': {'user': {'watching': {'totalCount': 28, 'nodes': [{'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}], 'pageInfo': {'hasNextPage': True, 'endCursor': 'MjA'}}}}}, {'data': {'user': {'watching': {'totalCount': 28, 'nodes': [{'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}, {'isFork': False}], 'pageInfo': {'hasNextPage': False, 'endCursor': 'Mjg'}}}}}],
    
    {'data': {'user': {'year2021': {'totalCommitContributions': 1850, 'totalPullRequestReviewContributions': 223, 'restrictedContributionsCount': 105}, 'year2020': {'totalCommitContributions': 1845, 'totalPullRequestReviewContributions': 92, 'restrictedContributionsCount': 0}, 'year2019': {'totalCommitContributions': 194, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2018': {'totalCommitContributions': 198, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2017': {'totalCommitContributions': 177, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2016': {'totalCommitContributions': 138, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2015': {'totalCommitContributions': 0, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2014': {'totalCommitContributions': 0, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2013': {'totalCommitContributions': 0, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2012': {'totalCommitContributions': 0, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}, 'year2011': {'totalCommitContributions': 0, 'totalPullRequestReviewContributions': 0, 'restrictedContributionsCount': 0}}}},

    [{'data': {'user': {'topRepositories': {'totalCount': 34, 'nodes': [{'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}], 'pageInfo': {'hasNextPage': True, 'endCursor': 'MTA'}}}}}, {'data': {'user': {'topRepositories': {'totalCount': 34, 'nodes': [{'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'someUserA'}}], 'pageInfo': {'hasNextPage': True, 'endCursor': 'MjA'}}}}}, {'data': {'user': {'topRepositories': {'totalCount': 34, 'nodes': [{'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'someUserA'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'someUserB'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'someUserC'}}, {'owner': {'login': 'someUserD'}}, {'owner': {'login': 'someUserE'}}], 'pageInfo': {'hasNextPage': True, 'endCursor': 'MzA'}}}}}, {'data': {'user': {'topRepositories': {'totalCount': 34, 'nodes': [{'owner': {'login': 'cicirello'}}, {'owner': {'login': 'cicirello'}}, {'owner': {'login': 'someUserA'}}, {'owner': {'login': 'someUserF'}}], 'pageInfo': {'hasNextPage': False, 'endCursor': 'MzQ'}}}}}]
    ]

class TestSomething(unittest.TestCase) :

    def test_parseQueryResults(self) :
        class NoQueries(Statistician) :
            def __init__(self, fail=True) :
                self.parseStats(
                    executedQueryResults[0],
                    executedQueryResults[1],
                    executedQueryResults[2],
                    executedQueryResults[4]
                    )
                self.parsePriorYearStats(executedQueryResults[3])
        stats = NoQueries()
        self._validate(stats)
    
    def test_parseQueryResultsMultipageQueryResults(self) :
        class NoQueriesMultipage(Statistician) :
            def __init__(self, fail=True) :
                self.parseStats(
                    executedQueryResultsMultiPage[0],
                    executedQueryResultsMultiPage[1],
                    executedQueryResultsMultiPage[2],
                    executedQueryResultsMultiPage[4]
                    )
                self.parsePriorYearStats(executedQueryResultsMultiPage[3])
        stats = NoQueriesMultipage()
        self._validate(stats)

    def test_color_themes(self) :
        originalThemes = {"light", "dark", "dark-dimmed"}
        for theme in originalThemes :
            self._colorValidation(colorMapping[theme])
        for theme in colorMapping :
            if theme not in originalThemes :
                self._colorValidation(colorMapping[theme])

    def test_title_templates(self) :
        unlikelyInTemplate = "qwertyuiop"
        try :
            for locale in supportedLocales :
                title = titleTemplates[locale].format(unlikelyInTemplate)
                self.assertTrue(title.find(unlikelyInTemplate)>=0)
        except IndexError :
            self.fail()

    def test_categories(self) :
        categories = {"general", "repositories", "contributions", "languages"}
        self.assertEqual(set(categoryOrder), categories)
        statistics = {
            "followers", "following", "sponsors", "sponsoring",
            "public", "starredBy",
            "forkedBy", "watchedBy", "templates", "archived", "commits",
            "issues", "prs", "reviews", "contribTo", "private"
            }
        
        # Make sure all are accounted for in a category
        statKeys = { stat for cat in categoryOrder for stat in statsByCategory[cat]}
        self.assertEqual(statistics, statKeys)

        # Make sure none are in more than one categories
        numStats = sum(len(statsByCategory[cat]) for cat in categoryOrder)
        self.assertEqual(numStats, len(statistics))

    def test_category_labels(self) :
        categories = categoryOrder
        types = {"heading", "column-one", "column-two"}
        for locale in supportedLocales :
            self.assertTrue(locale in categoryLabels)
            labelMap = categoryLabels[locale]
            for cat in categories :
                self.assertTrue(cat in labelMap)
                for t in types :
                    self.assertTrue(t in labelMap[cat])
                    
    def test_stat_labels(self) :
        keys = {
            "followers", "following", "sponsors", "sponsoring",
            "public", "starredBy",
            "forkedBy", "watchedBy", "templates", "archived", "commits",
            "issues", "prs", "reviews", "contribTo", "private"
            }
        self.assertTrue(all(k in statLabels for k in keys))
        for k in keys :
            self.assertTrue("icon" in statLabels[k])
            self.assertTrue(statLabels[k]["icon"].startswith("<path "))
            self.assertTrue(statLabels[k]["icon"].endswith("/>"))
            labelsByLocale = statLabels[k]["label"]
            for locale in supportedLocales :
                self.assertTrue(locale in labelsByLocale)

    def test_generateSVG(self) :
        class NoQueries(Statistician) :
            def __init__(self, fail=True) :
                self.parseStats(
                    executedQueryResultsTest2[0],
                    executedQueryResultsTest2[1],
                    executedQueryResultsTest2[2],
                    executedQueryResultsTest2[4]
                    )
                self.parsePriorYearStats(executedQueryResultsTest2[3])
        stats = NoQueries()
        svgGen = StatsImageGenerator(stats, copy.deepcopy(colorMapping["light"]), "en", 6, 18)
        #print(svgGen.generateImage(True, None, {}))

    def _colorValidation(self, theme) :
        props = {"bg", "border", "icons", "text", "title"}
        validHexDigits = set("0123456789abcdefABCDEF")
        for p in props :
            color = theme[p]
            self.assertEqual("#", color[0])
            self.assertTrue(len(color)==4 or len(color)==7)
            self.assertTrue(all(c in validHexDigits for c in color[1:]))

    def _validate(self, stats) :
        self.assertEqual(9, stats._user["followers"][0])
        self.assertEqual(7, stats._user["following"][0])
        self.assertEqual(7, stats._user["sponsors"][0])
        self.assertEqual(5, stats._user["sponsoring"][0])
        self.assertEqual(29, stats._repo["public"][0])
        self.assertEqual(31, stats._repo["public"][1])
        self.assertEqual(36, stats._repo["starredBy"][0])
        self.assertEqual(36, stats._repo["starredBy"][1])
        self.assertEqual(28, stats._repo["forkedBy"][0])
        self.assertEqual(28, stats._repo["forkedBy"][1])
        self.assertEqual(3, stats._repo["watchedBy"][0])
        self.assertEqual(3, stats._repo["watchedBy"][1])
        self.assertEqual(2, stats._repo["archived"][0])
        self.assertEqual(2, stats._repo["archived"][1])
        self.assertEqual(1, stats._repo["templates"][0])
        self.assertEqual(1, stats._repo["templates"][1])
        self.assertEqual(3602, stats._contrib["commits"][0])
        self.assertEqual(4402, stats._contrib["commits"][1])
        self.assertEqual(79, stats._contrib["issues"][0])
        self.assertEqual(81, stats._contrib["issues"][1])
        self.assertEqual(289, stats._contrib["prs"][0])
        self.assertEqual(289, stats._contrib["prs"][1])
        self.assertEqual(315, stats._contrib["reviews"][0])
        self.assertEqual(315, stats._contrib["reviews"][1])
        self.assertEqual(3, stats._contrib["contribTo"][0])
        self.assertEqual(8, stats._contrib["contribTo"][1])
        self.assertEqual(105, stats._contrib["private"][0])
        self.assertEqual(105, stats._contrib["private"][1])
        total = 5222379
        self.assertEqual(total, stats._languages["totalSize"])
        self.assertEqual(11, len(stats._languages["languages"]))
        expectedLanguages = [
            "Java",
            "HTML",
            "Python",
            "TeX",
            "Dockerfile",
            "Makefile",
            "Shell",
            "GraphQL",
            "CSS",
            "JavaScript",
            "Batchfile"
            ]
        expectedColors = [
            '#b07219',
            '#e34c26',
            '#3572A5',
            '#3D6117',
            '#384d54',
            '#427819',
            '#89e051',
            '#e10098',
            '#563d7c',
            '#f1e05a',
            '#C1F12E'
            ]
        expectedSize = [3385976, 1343301, 274535, 202824, 5448, 4442, 1926, 1902, 1721, 204, 100]
        for i, L in enumerate(stats._languages["languages"]) :
            self.assertEqual(expectedLanguages[i], L[0])
            self.assertEqual(expectedColors[i], L[1]["color"])
            self.assertEqual(expectedSize[i], L[1]["size"])
            self.assertAlmostEqual(expectedSize[i]/total, L[1]["percentage"], places=5)
            
        
