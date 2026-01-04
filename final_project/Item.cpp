#include "Item.h"
#include <stdexcept>
#include <sstream>

using namespace std;

Item::Item(int id,const string& name): id(id), name(name), isBorrowed(false), borrowedBy(""){}

int Item::getId() const{
    return id;
}

