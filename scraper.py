#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://github.com/topics')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
repo = soup.find(class_="col-lg-9 position-relative pr-lg-5 mb-6 mr-lg-5")

# find all instances of that class (should return 25 as shown in the github main page)
repo_list = repo.find_all(class_="py-4 border-bottom d-flex flex-justify-between")

print(len(repo_list))

file_name = "github_trending_today.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))
f.writerow(['Topic', 'Link'])

for repo in repo_list:
    topic = repo.find('p').text
    link = repo.find('a').href
    f.writerow([topic, link])


    
    void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        int pi = partition(arr, low, high);
 
        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
 
/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
 
// Driver program to test above functions
int main()
{
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr)/sizeof(arr[0]);
    quickSort(arr, 0, n-1);
    printf("Sorted array: \n"
