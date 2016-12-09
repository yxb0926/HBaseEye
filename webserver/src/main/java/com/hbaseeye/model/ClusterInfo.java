package com.hbaseeye.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

/**
 * Created by yuanxiaobin on 16/12/9.
 */

@Document(collection = "clusterInfo") // 指定collection
public class ClusterInfo {

    @Id
    private String _id;
    private int numRegionServers;
    private long timestamp;
    private String serverName;
    private String hostname;
    private String clusterId;
    private long clusterRequests;
    private long masterActiveTime;
    private String role;
    private int numDeadRegionServers;
    private long masterStartTime;
    private String isActiveMaster;

    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }

    public int getNumRegionServers() {
        return numRegionServers;
    }

    public void setNumRegionServers(int numRegionServers) {
        this.numRegionServers = numRegionServers;
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

    public String getClusterId() {
        return clusterId;
    }

    public void setClusterId(String clusterId) {
        this.clusterId = clusterId;
    }

    public long getClusterRequests() {
        return clusterRequests;
    }

    public void setClusterRequests(long clusterRequests) {
        this.clusterRequests = clusterRequests;
    }

    public long getMasterActiveTime() {
        return masterActiveTime;
    }

    public void setMasterActiveTime(long masterActiveTime) {
        this.masterActiveTime = masterActiveTime;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public int getNumDeadRegionServers() {
        return numDeadRegionServers;
    }

    public void setNumDeadRegionServers(int numDeadRegionServers) {
        this.numDeadRegionServers = numDeadRegionServers;
    }

    public long getMasterStartTime() {
        return masterStartTime;
    }

    public void setMasterStartTime(long masterStartTime) {
        this.masterStartTime = masterStartTime;
    }

    public String getIsActiveMaster() {
        return isActiveMaster;
    }

    public void setIsActiveMaster(String isActiveMaster) {
        this.isActiveMaster = isActiveMaster;
    }
}
