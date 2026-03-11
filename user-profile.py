user = {
    'name': 'Alice',
    'degree': 'MSc Computer Science',
    'status': 'Active'
}

print(user['degree'])   # prints: MSc Computer Science

# safer access if the key might be missing:
print(user.get('degree'))