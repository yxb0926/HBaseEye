package com.hbaseeye.service;

import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Created by yuanxiaobin on 16/12/2.
 */
@Service
public interface RequestService {
    public List getQps(String hostname, long starttime, long endtime);
    public List getTps(String hostname, int timestamp);
    public List getRead(String hostname, int timestamp);
    public List getWrite(String hostname, int timestamp);
    public List totalRequestCount(String hostname, int timestamp);
    public List readRequestCount(String hostname, int timestamp);
    public List writeRequestCount(String hostname, int timestamp);

}
