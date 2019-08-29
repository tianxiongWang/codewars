    double high(double, double, double, int);
    int count;
    if (h > 0 && bounce > 0 && bounce < 1 && window < h)
    {
        if (h >= window)
            count += 1;
        while (true)
        {
            h *= bounce;
            if (h > window)
                count += 2;
            else
                break;
        }
        return count;
    }
    else
    {
        return -1;
    }