package com.hbaseeye.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

/**
 * Created by yuanxiaobin on 16/12/12.
 */
@Document(collection = "regionInfo") // 指定collection
public class RegionInfo {
    @Id
    String _id;
    long timestamp;
    String serverName;
    String hostname;
    String liveRegionServer;
    long   read;
    long   write;
    long   totalRequestCount;
    int    regionCount;
    int    storeFileCount;
    int    memStoreSize;
    int    storeFileSize;

    public int getStoreFileSize() {
        return storeFileSize;
    }

    public void setStoreFileSize(int storeFileSize) {
        this.storeFileSize = storeFileSize;
    }

    public int getStoreFileCount() {
        return storeFileCount;
    }

    public void setStoreFileCount(int storeFileCount) {
        this.storeFileCount = storeFileCount;
    }

    public int getMemStoreSize() {
        return memStoreSize;
    }

    public void setMemStoreSize(int memStoreSize) {
        this.memStoreSize = memStoreSize;
    }

    public int getRegionCount() {
        return regionCount;
    }

    public void setRegionCount(int regionCount) {
        this.regionCount = regionCount;
    }

    public long getRead() {
        return read;
    }

    public void setRead(long read) {
        this.read = read;
    }

    public long getWrite() {
        return write;
    }

    public void setWrite(long write) {
        this.write = write;
    }

    public long getTotalRequestCount() {
        return totalRequestCount;
    }

    public void setTotalRequestCount(long totalRequestCount) {
        this.totalRequestCount = totalRequestCount;
    }

    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) {
        this.timestamp = timestamp;
    }

    public String getServerName() {
        return serverName;
    }

    public void setServerName(String serverName) {
        this.serverName = serverName;
    }

    public String getHostname() {
        return hostname;
    }

    public void setHostname(String hostname) {
        this.hostname = hostname;
    }

    public String getLiveRegionServer() {
        return liveRegionServer;
    }

    public void setLiveRegionServer(String liveRegionServer) {
        this.liveRegionServer = liveRegionServer;
    }
}
