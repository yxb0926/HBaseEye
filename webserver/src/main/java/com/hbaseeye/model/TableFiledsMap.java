package com.hbaseeye.model;

/**
 * Created by yuanxiaobin on 16/12/12.
 */
public class TableFiledsMap {
    public String tableName;
    public String filedName;

    public TableFiledsMap(String tableName, String filedName){
        this.tableName = tableName;
        this.filedName = filedName;
    }

    public String getTableName() {
        return tableName;
    }

    public void setTableName(String tableName) {
        this.tableName = tableName;
    }

    public String getFiledName() {
        return filedName;
    }

    public void setFiledName(String filedName) {
        this.filedName = filedName;
    }
}
